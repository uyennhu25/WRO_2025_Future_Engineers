import sensor, image, time
import LPF2

# === LUMP Define ===
modes = [LPF2.mode('OpenMV-ALL',size = 8, type = LPF2.DATA16, format = '3.0'),]
DataToSend = [0, 0, 0, 0, 0, 0, 0, 0] #X, Y, W, H, ID, state, 0, 0
max_idx = -1
lpf2 = LPF2.Prime_LPF2(3, 'P4', 'P5', modes, 62, timer = 4, freq =10)
lpf2.initialize()

# === Camera setup ===
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)  # 320x240
sensor.skip_frames(time=2000)
clock = time.clock()

# === Color thresholds (tune these using Threshold Editor) ===
red_threshold   = (30, 100, 15, 127, 15, 127)
green_threshold = (30, 100, -128, -20, -128, 127)
black_thresh = [(0, 50, -128, 127, -128, 127)]

# === Diagonal line parameters ===
center_x = 160  # middle of the image

# Left diagonal (red side)
m_left = 240 / 160  # slope
b_left = 240

#Define the middle ROI
mid_roi = (110, 120, 100, 50)

# Right diagonal (green side)
m_right = 240 / 160
b_right = -m_right * 160  # ensures line passes top center

# === Helper functions ===
def y_on_left_line(x): return -m_left * x + b_left
def y_on_right_line(x): return m_right * x + b_right
def distance_to_left_line(x, y): return y - y_on_left_line(x)
def distance_to_right_line(x, y): return y - y_on_right_line(x)

while True:
    clock.tick()
    img = sensor.snapshot().rotation_corr(z_rotation=180)


    # --- MID ROI ---
    mid_blobs = img.find_blobs(black_thresh, roi=mid_roi, pixels_threshold=5, area_threshold=5, merge=True)
    mid_black_pixels = sum([b.pixels() for b in mid_blobs])
    mid_total_pixels =  mid_roi[2] *  mid_roi[3]
    mid_black_percent = ( mid_black_pixels /  mid_total_pixels) * 100



    # Draw reference lines
    img.draw_line([0, 240, 160, 0], color=(255, 0, 0))   # left red diagonal
    img.draw_line([160, 0, 320, 240], color=(0, 255, 0)) # right green diagonal
    img.draw_line([160, 0, 160, 240], color=(255, 255, 255)) # center

    # Find all color blobs
    blobs = img.find_blobs([red_threshold, green_threshold],
                           pixels_threshold=200,
                           area_threshold=200,
                           merge=True)

    if blobs:
        # Find the biggest blob (the one with largest area)
        largest_blob = max(blobs, key=lambda b: b.pixels())

        # Draw bounding box and center
        img.draw_rectangle(largest_blob.rect())
        img.draw_cross(largest_blob.cx(), largest_blob.cy())

        # Bottom center of bounding box
        bottom_x = largest_blob.cx()
        bottom_y = largest_blob.y() + largest_blob.h()
        img.draw_cross(bottom_x, bottom_y, color=(255, 255, 255))

        # Identify color and calculate error
        if largest_blob.code() == 1:  # Red
            error = distance_to_left_line(bottom_x, bottom_y)
            img.draw_string(bottom_x, bottom_y - 10,
                            "RED Err: %.1f" % error, color=(255, 0, 0))
            print("Largest: RED | Error:", error)

        elif largest_blob.code() == 2:  # Green
            error = distance_to_right_line(bottom_x, bottom_y)
            img.draw_string(bottom_x, bottom_y - 10,
                            "GRN Err: %.1f" % error, color=(0, 255, 0))
            print("Largest: GREEN | Error:", error)

        DataToSend=[error, mid_black_percent]
        mode=lpf2.current_mode
        if mode==0:
            lpf2.load_payload('Int16', DataToSend)

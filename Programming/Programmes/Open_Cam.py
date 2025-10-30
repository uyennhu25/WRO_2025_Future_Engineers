import sensor, time
import LPF2

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time=2000)

clock = time.clock()

##LUMP Define
modes = [LPF2.mode('OpenMV-ALL',size = 8, type = LPF2.DATA16, format = '3.0'),]
DataToSend = [0, 0, 0, 0, 0, 0, 0, 0] #X, Y, W, H, ID, state, 0, 0
max_idx = -1
lpf2 = LPF2.Prime_LPF2(3, 'P4', 'P5', modes, 62, timer = 4, freq =10)
lpf2.initialize()

# Define ROIs
left_roi = (0, 60, 60, 120)
right_roi = (260, 60, 60, 120)
mid_roi = (110, 120, 100, 50)

black_thresh = [(0, 50, -128, 127, -128, 127)]

while True:
    clock.tick()
    img = sensor.snapshot().rotation_corr(z_rotation=180)

    # Draw ROIs
    img.draw_rectangle(left_roi, color=(255, 0, 0))
    img.draw_rectangle(right_roi, color=(255, 0, 0))
    img.draw_rectangle(mid_roi, color=(255, 0, 0))

    # --- LEFT ROI ---
    left_blobs = img.find_blobs(black_thresh, roi=left_roi, pixels_threshold=5, area_threshold=5, merge=True)
    left_black_pixels = sum([b.pixels() for b in left_blobs])
    left_total_pixels = left_roi[2] * left_roi[3]
    left_black_percent = (left_black_pixels / left_total_pixels) * 100

    # --- RIGHT ROI ---
    right_blobs = img.find_blobs(black_thresh, roi=right_roi, pixels_threshold=5, area_threshold=5, merge=True)
    right_black_pixels = sum([b.pixels() for b in right_blobs])
    right_total_pixels = right_roi[2] * right_roi[3]
    right_black_percent = (right_black_pixels / right_total_pixels) * 100

    # --- MID ROI ---
    mid_blobs = img.find_blobs(black_thresh, roi=mid_roi, pixels_threshold=5, area_threshold=5, merge=True)
    mid_black_pixels = sum([b.pixels() for b in mid_blobs])
    mid_total_pixels =  mid_roi[2] *  mid_roi[3]
    mid_black_percent = ( mid_black_pixels /  mid_total_pixels) * 100

    print("Left:", left_black_percent, " Right:", right_black_percent, " Middle:", mid_black_percent)

    DataToSend = [left_black_percent, right_black_percent, mid_black_percent]
    mode=lpf2.current_mode
    if mode==0:
        lpf2.load_payload('Int16', DataToSend)

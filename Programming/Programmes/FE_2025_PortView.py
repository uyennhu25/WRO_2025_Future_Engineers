from FE_Functions import*
while True: 
    Cam_val = Camera.read(0) 
    Color_val = SenRaw.read(5)
    Ultra_val = Ultrasonic.read(0)
    print("Color: ", Cam_val[0], "X: ", Cam_val[1], "Width: ", Cam_val[2], "Wall: ", Cam_val[3])
    print("R: ", Color_val[0], "G: ", Color_val[1], "B: ", Color_val[2], "W: ", Color_val[3])
    print(Ultra_val[0])
    wait(500)



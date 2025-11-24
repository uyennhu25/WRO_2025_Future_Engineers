from FE_Functions import*
hub.imu.reset_heading(0)
heading = 0 
SteerDirection = 0 
ColorCondition = 0
Cam_val = Camera.read(0)
Drive.dc(100)

Add = 200 if Cam_val[0]>10 and Cam_val[1]>10 else 0
while GetColor() == 0:
    steering(0)
Drive.reset_angle(0)
while abs(Drive.angle()) < Add:
    steering(0)

if GetColor() == 1:
    ColorCondition = 1
    Plus = -30
else:
    ColorCondition = -1
    Plus = 40
print(ColorCondition)
for i in range (11):
    while GetColor() != ColorCondition:
        SteerCamOpen(ColorCondition, Plus)
    while GetColor() == ColorCondition:
        SteerCamOpen(ColorCondition, Plus)
Drive.reset_angle(0)
while abs(Drive.angle()) < 2000:
    SteerCamOpen(ColorCondition, Plus)

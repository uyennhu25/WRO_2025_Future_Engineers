from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, multitask, run_task
from pybricks.iodevices import PUPDevice
from umath import sin, cos, radians, atan2, degrees
global hub, motorB, motorC, motorA, motorD, motorE, dBase, Stuckmera, ColorCondition, LineCount

# Configuration
hub = PrimeHub()
hub.system.set_stop_button(Button.BLUETOOTH) #use bluetooth button to end the program
hub.speaker.volume(50) 
Steer = Motor(Port.A)
Drive = Motor(Port.C)
Camera = PUPDevice(Port.B)
Sen = ColorSensor(Port.E)
SenRaw = PUPDevice(Port.E)
Ultrasonic = PUPDevice(Port.D)
ColorCondition = 0 
LineCount = 0 

# IMU 
def Compass():
    compass = ((hub.imu.heading() % 360) + 360) % 360
    return compass

def AD_angle():
    compass = Compass()
    theta = compass if compass <= 180 else compass - 360
    return theta 

def RD_angle(angle):
    compass = (((hub.imu.heading() - angle) % 360) + 360) % 360
    zeta = compass if compass <= 180 else compass - 360
    return zeta 

# Driving
def steering(angle): 
    target = -RD_angle(angle)*3
    target = target if target < 140 and target >-140 else 140 * target/abs(target)
    pwr = (target - Steer.angle()) * 7
    if abs(pwr) < 20 and abs(pwr) > 1: pwr = pwr/abs(pwr)*20
    Steer.dc(pwr)
    return(pwr)

def SteerCamOpen(ColorCondition, Plus):
    Cam_val = Camera.read(0)
    # print(Cam_val[0], Cam_val[1])
    
    target = (Cam_val[0] - Cam_val[1] - ColorCondition*Plus)*1 if (Cam_val [0] < 25 or Cam_val [1] < 25) else ColorCondition*-1000
    target = target if (target < 140 and target >-140) else 140 * target/abs(target)
    pwr = (target - Steer.angle())
    if abs(pwr) < 30 and abs(pwr) > 3: pwr = pwr/abs(pwr)*30
    Steer.dc(pwr)
    return(pwr)
    

def SteerCamObstacle (Sign, Plus):
    Cam_val = Camera.read(0)
    if Cam_val[0] == 0:
        target = (Cam_val[3]- ColorCondition*Plus)*5 if Cam_val[3] != 1000 else Sign*-1000
        target = target if (target < 140 and target >-140) else 140 * target/abs(target)
        pwr = (target - Steer.angle())*1.5
        if abs(pwr) < 30 and abs(pwr) > 3: pwr = pwr/abs(pwr)*30
        Steer.dc(pwr)
    else:
        target = Cam_val[1] - 160 
        target = target if (target < 140 and target >-140) else 140 * target/abs(target) 
        pwr = (target - Steer.angle())
        if abs(pwr) < 30 and abs(pwr) > 3: pwr = pwr/abs(pwr)*30
        Steer.dc(pwr)
    return(pwr)

def BackDown():
    Drive.reset_angle()
    Drive.stop()
    wait(50)
    while abs(Drive.angle())<300:
        Drive.dc(-70)
        target = 0 
        pwr = (target - Steer.angle())
        if abs(pwr) < 30 and abs(pwr) > 3: pwr = pwr/abs(pwr)*30
        Steer.dc(pwr)
    Drive.stop()
    wait(50)

def Avoid():
    Cam_val = Camera.read(0)
    tempimu = hub.imu.heading()
    Drive.dc(50)
    if Cam_val[0] == 3:
        while hub.imu.heading()>tempimu-47:
            target = -140
            pwr = (target - Steer.angle())
            Steer.dc(pwr)
        while hub.imu.heading()<tempimu-40*ColorCondition:
            Drive.dc(50)
            target = 140
            pwr = (target - Steer.angle())
            Steer.dc(pwr)
    else: 
        while hub.imu.heading()<tempimu+47:
            target = 140
            pwr = (target - Steer.angle())
            Steer.dc(pwr)
        while hub.imu.heading()>tempimu-40*ColorCondition:
            Drive.dc(50)
            target = -140
            pwr = (target - Steer.angle())
            Steer.dc(pwr)
    Drive.dc(70)

def Move_Gyro(pwr, target):
    speed = pwr - 0.7*pwr*abs(steering(target))/140
    if abs(speed) < 30 and speed != 0: speed = speed/abs(speed)*30
    Drive.dc(speed)

def Move_Gyro_deg(pwr, target, degree):
    enc = Drive.angle()
    Drive.reset_angle(0)
    while abs(Drive.angle()) < degree:
        Move_Gyro(pwr, target)
    Drive.reset_angle(enc + Drive.angle())
    
def SteerTo(goal):
    target = goal
    pwr = (goal - Steer.angle())
    while abs(pwr) > 5:
        pwr = (target - Steer.angle())
        Steer.dc(pwr)
    Steer.hold()    

#ColorSensor
# rgbw / white/ orange/ blue
# 875/930/1010/1010
# 665/310/355/1000 
# 141/160/269/400
def checkColor():
    array = [0,0,0,0,0,0,0]
    color = 6
    for i in range(10):
        raw = SenRaw.read(5) 
        if raw[2] < 800:
            color  = 4 if raw[0] > raw[2] else 2
        array[color] = array[color]+1
    MaxVal = 0; MaxInd = 0
    for i in range(7):
        if array[i]> MaxVal: 
            MaxVal = array[i]; MaxInd = i
    return(MaxInd)

def CheckLine():
    color = checkColor() 
    if color != 6:
        turn = 1 if color == 4 else -1
        return(turn)
    else: return(0)       

def GetColor():
    Color_val = SenRaw.read(5)
    if Color_val[0] < Color_val[1] and Color_val[1] < 900: 
        Out = 1 #Blue
    elif Color_val[0] > Color_val[1] and Color_val[1] < 900:
        Out = -1 #Orange 
    else:
        Out = 0 #White
    return Out

def ColorCount():
    LineCount = 0
    c = GetColor()
    while c == 0:
        c = GetColor()

    last = c  # last color seen

    while True:
        c = GetColor()

        if last != ColorCondition and c == ColorCondition:
            LineCount += 1
            print("Count =", LineCount)

        last = c
        wait(10)

def FEDrive():
    ColorCondition = 1
    print(ColorCondition)
    while LineCount < 11:
        while True:
            Drive.dc(70)
            Cam_val = Camera.read(0)
            SteerCamObstacle(ColorCondition,80)
            if Cam_val[2] > 75 or LineCount >= 11:
                break
        if Cam_val[2] < 95:
            Avoid()
        elif LineCount >= 11:
            None
        else:
            BackDown()

def RunDeg(pwr, enc):
    Drive.reset_angle(0)
    while abs(abs(Drive.angle()) - enc) > 3:
        Drive.dc(pwr)

def GetOut():
    Ultra_val = Ultrasonic.read(0)
    if Ultra_val[0] <150:
        ColorCondition = 1
        Steer.dc(-90)
        wait(100)
        RunDeg(50,130)
        Drive.hold()
        wait(50)
        Steer.dc(90)
        wait(300)
        RunDeg(-60, 70)
        Drive.hold()
        wait(50)   
        Steer.dc(-90)
        wait(100)
        RunDeg(40,200)
    else: 
        ColorCondition = -1
        Steer.dc(90)
        wait(100)
        RunDeg(50,130)
        Drive.hold()
        wait(50)
        Steer.dc(-90)
        wait(300)
        RunDeg(-60, 70)
        Drive.hold()
        wait(50)   
        Steer.dc(90)
        wait(100)
        RunDeg(40,200)
        Steer.dc(-90)
        RunDeg(50,100)




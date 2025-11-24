from FE_Functions_2 import*
hub.imu.reset_heading(0)
heading = 0         
i = 0 
Ultra_val = Ultrasonic.read(0)

GetOut()
FEDrive(1.5)
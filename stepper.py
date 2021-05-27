import RPi.GPIO as GPIO

# import the library
from RpiMotorLib import RpiMotorLib

GpioPins = [6, 13, 19, 26]

# Declare an named instance of class pass a name and motor type
mymotortest = RpiMotorLib.BYJMotor("MyMotorOne", "28BYJ")

# call the function pass the parameters
mymotortest.motor_run(GpioPins , .001, 1024, False, False, "full", .05)

# good practise to cleanup GPIO at some point before exit
GPIO.cleanup()
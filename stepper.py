import RPi.GPIO as GPIO

# import the library
from RpiMotorLib import RpiMotorLib

#
gpioPins = [5, 6, 19, 26]

# Declare an named instance of class pass a name and motor type
myMotor = RpiMotorLib.BYJMotor("MyMotor", "Nema")

# call the function pass the parameters
myMotor.motor_run(gpioPins, 0.001, 1024, False, False, "full", 0.05)

# good practise to cleanup GPIO at some point before exit
GPIO.cleanup()

#PWM test






import RPi.GPIO as GPIO
from time import sleep

SpeedPin = 19
SpeedPin1 = 13

SpeedPinA = 18
SpeedPinA1 = 12



DirectionPin1 = 4
DirectionPin2 = 17

DirectionPin3 = 3
DirectionPin4 = 2  

GPIO.setwarnings(False)			#disable warnings
GPIO.setmode(GPIO.BCM)	#set pin numbering system

GPIO.cleanup()

GPIO.setup(SpeedPin,GPIO.OUT)

GPIO.setup(SpeedPin1,GPIO.OUT)

GPIO.setup(SpeedPinA,GPIO.OUT)

GPIO.setup(SpeedPinA1,GPIO.OUT)

GPIO.setup(DirectionPin1,GPIO.OUT)

GPIO.setup(DirectionPin2,GPIO.OUT)

GPIO.setup(DirectionPin3,GPIO.OUT)

GPIO.setup(DirectionPin4,GPIO.OUT)


pi_pwm = GPIO.PWM(SpeedPin,1000)		#create PWM instance with frequency
pi_pwm.start(0)

pi_pwm1 = GPIO.PWM(SpeedPin1,1000)		#create PWM instance with frequency
pi_pwm1.start(0)	

pi_pwmA1 = GPIO.PWM(SpeedPinA,1000)		#create PWM instance with frequency
pi_pwmA1.start(0)

pi_pwmA2 = GPIO.PWM(SpeedPinA1,1000)	#create PWM instance with frequency
pi_pwmA2.start(0)


GPIO.output(DirectionPin1, True)

GPIO.output(DirectionPin2, True)

GPIO.output(DirectionPin3, False)

GPIO.output(DirectionPin4, False)


#start PWM of required Duty Cycle 
def TurnLeft():
    print("Turning Left")
    SpeedPin.ChangeDutyCycle(100)

def TurnRight():
    print("Turning Right")
    SpeedPin1.ChangeDutyCycle(100)

def GoForward():
    print("Going Forward")
    SpeedPinA.ChangeDutyCycle(100)

def GoBackward():
    print("reversing")
    SpeedPinA1.ChangeDutyCycle(100)

    
while True:
    value = input()
    if value == "w":
        GoForward()
    if value == "s":
        GoBackward()
    if value == "a":
        TurnLeft()
    if value == "d":
        TurnRight()
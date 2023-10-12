#PWM test






import RPi.GPIO as GPIO
from time import sleep

SpeedPin = 12
SpeedPin1 = 13
# PWM pins


SpeedPinA = 18
SpeedPinA1 = 19

DirectionPin = 4
DirectionPin1 = 17

DirectionPinA = 3
DirectionPinA1 = 2

GPIO.setwarnings(False)			#disable warnings
GPIO.setmode(GPIO.BOARD)	#set pin numbering system

GPIO.cleanup()

GPIO.setup(SpeedPin,GPIO.OUT)
GPIO.setup(SpeedPin1,GPIO.OUT)

GPIO.setup(SpeedPinA,GPIO.OUT)
GPIO.setup(SpeedPinA1,GPIO.OUT)

GPIO.setup(DirectionPin,GPIO.OUT)
GPIO.setup(DirectionPin1,GPIO.OUT)

GPIO.setup(DirectionPinA,GPIO.OUT)
GPIO.setup(DirectionPinA1,GPIO.OUT)


pi_pwm = GPIO.PWM(SpeedPin,1000)		#create PWM instance with frequency
pi_pwm.start(0)

pi_pwm1 = GPIO.PWM(SpeedPin1,1000)		#create PWM instance with frequency
pi_pwm1.start(0)	

pi_pwmA1 = GPIO.PWM(SpeedPinA,1000)		#create PWM instance with frequency
pi_pwmA1.start(0)

pi_pwmA2 = GPIO.PWM(SpeedPinA1,1000)		#create PWM instance with frequency
pi_pwmA2.start(0)

GPIO.output(DirectionPin, True)
GPIO.output(DirectionPin1, True)

GPIO.output(DirectionPinA, True)
GPIO.output(DirectionPinA1, True)


#start PWM of required Duty Cycle 
while True:
    for duty in range(0,101,1):
        pi_pwm.ChangeDutyCycle(duty) #provide duty cycle in the range 0-100
        pi_pwm1.ChangeDutyCycle(duty)
        pi_pwmA1.ChangeDutyCycle(duty)
        sleep(0.1)
                
    for duty in range(100,0,-1):
        pi_pwm.ChangeDutyCycle(duty)
        pi_pwm1.ChangeDutyCycle(duty)
        pi_pwmA2.ChangeDutyCycle(duty)
        sleep(0.1)
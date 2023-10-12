#PWM test






import RPi.GPIO as GPIO
from time import sleep

SpeedPin = 19
SpeedPin1 = 13

SpeedPinA = 18
SpeedPinA1 = 12



DirectionPin = 4
DirectionPin1 = 17

DirectionPinA = 3
DirectionPinA1 = 2  

GPIO.setwarnings(False)			#disable warnings
GPIO.setmode(GPIO.BCM)	#set pin numbering system

GPIO.cleanup()

GPIO.setup(SpeedPin,GPIO.OUT)
GPIO.setup(SpeedPin1,GPIO.OUT)

GPIO.setup(SpeedPinA,GPIO.OUT)
GPIO.setup(SpeedPinA1,GPIO.OUT)

GPIO.setup(DirectionPin,GPIO.OUT)
GPIO.setup(DirectionPin1,GPIO.OUT)

GPIO.setup(DirectionPinA,GPIO.OUT)
GPIO.setup(DirectionPinA1,GPIO.OUT)


pi_pwm = GPIO.PWM(SpeedPin,10000)		#create PWM instance with frequency
pi_pwm.start(0)

pi_pwm1 = GPIO.PWM(SpeedPin1,10000)		#create PWM instance with frequency
pi_pwm1.start(0)	

pi_pwmA1 = GPIO.PWM(SpeedPinA,10000)		#create PWM instance with frequency
pi_pwmA1.start(0)

pi_pwmA2 = GPIO.PWM(SpeedPinA1,10000)	#create PWM instance with frequency
pi_pwmA2.start(0)


GPIO.output(DirectionPin, True)
GPIO.output(DirectionPin1, True)

GPIO.output(DirectionPinA, True)
GPIO.output(DirectionPinA1, True)


#start PWM of required Duty Cycle 
while True:
    for duty in range(100):
        pi_pwm.ChangeDutyCycle(duty) #provide duty cycle in the range 0-100
        pi_pwm1.ChangeDutyCycle(duty)
        pi_pwmA1.ChangeDutyCycle(duty)
        pi_pwmA2.ChangeDutyCycle(duty)
        #sleep(0.1)
                
    for duty in range(100):
        pi_pwm.ChangeDutyCycle(duty)
        pi_pwm1.ChangeDutyCycle(duty)
        pi_pwmA1.ChangeDutyCycle(duty)
        pi_pwmA2.ChangeDutyCycle(duty)
        #sleep(0.1)
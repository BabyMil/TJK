import RPi.GPIO as GPIO
import time

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin you're using
servo_pin = 17

# Set the GPIO pin as an output
GPIO.setup(servo_pin, GPIO.OUT)

# Create a PWM instance with a frequency of 50 Hz
pwm = GPIO.PWM(servo_pin, 50)

# Start PWM with a duty cycle of 0 (servo at 0 degrees)
pwm.start(0)

try:
    while True:
        # Ask the user for the angle (0 to 180 degrees)
        angle = float(input("Enter angle (0 to 180 degrees): "))
        
        # Map the angle to the duty cycle (2.5 to 12.5)
        duty_cycle = (angle / 18) + 2.5
        
        # Change the servo position
        pwm.ChangeDutyCycle(duty_cycle)
        
        time.sleep(1)  # Pause for 1 second
        
except KeyboardInterrupt:
    # Clean up and exit on Ctrl+C
    pwm.stop()
    GPIO.cleanup()
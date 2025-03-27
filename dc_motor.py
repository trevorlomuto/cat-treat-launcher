import RPi.GPIO as GPIO
import time

# Set up GPIO pins
IN1 =  4  # GPIO pin for IN1
IN2 = 14  # GPIO pin for IN2

GPIO.setmode(GPIO.BCM)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)

try:
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    print("Motor should be moving forward...")
    time.sleep(5)  # Run for 5 seconds
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    print("Motor stopped.")
finally:
    GPIO.cleanup()



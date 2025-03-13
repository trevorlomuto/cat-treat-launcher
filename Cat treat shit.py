import sys
import time
import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib

# Pin configuration (Update these with actual GPIO pin numbers)
STEPPER_PINS = [17, 18, 27, 22]  # Example GPIO pins for ULN2003
DC_MOTOR_PIN = 23  # Example GPIO pin for DRV8871
REMOTE_BUTTON_PIN = 24  # Example GPIO pin for remote button

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(DC_MOTOR_PIN, GPIO.OUT)
GPIO.setup(REMOTE_BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Initialize stepper motor
stepper = RpiMotorLib.BYJMotor("StepperMotor", "28BYJ")
    
def loadtreat():
    """Loads the treat into the hopper using stepper motor."""
    print("Loading treat...")
    stepper.motor_run(STEPPER_PINS, 0.001, 512, False, False, "full", 0.05)  # Adjust as needed
    time.sleep(1)

def launchtreat():
    """Launches the treat using the DC motor."""
    print("Launching treat...")
    GPIO.output(DC_MOTOR_PIN, GPIO.HIGH)
    time.sleep(0.5)  # Adjust duration as needed
    GPIO.output(DC_MOTOR_PIN, GPIO.LOW)

def Pressremote():
    """Detects button press and triggers treat dispense sequence."""
    while True:
        if GPIO.input(REMOTE_BUTTON_PIN) == GPIO.HIGH:
            print("Button pressed! Dispensing treat...")
            loadtreat()
            time.sleep(1)  # Delay before launching
            launchtreat()
        time.sleep(0.1)  # Polling delay

if __name__ == "__main__":
    try:
        print("Waiting for remote signal...")
        Pressremote()
    except KeyboardInterrupt:
        print("Exiting program...")
    finally:
        GPIO.cleanup()







"""
def greet(name: str) -> None:
    print(f"Hello, {name}!")

# Example usage:
greet("John")



def isLeapYear(year):
     if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
          return True
     else:
          return False

#date = input("please enter date in MM/DD/YYYY")

        #0123456789
date =  "10/01/2024"

month = int(date[0:2])  # MM
day = int(date[3:5])    # DD
year = int(date[6:])    # YYYY

print(month,day,year)

#if its a 30 day month
if month == 9 or  month == 4 or month == 6 or month == 11:
    print("valid 30 day month")
    if   1 <= day <= 30:
         print("day is invalid")
    else:
        print("day is valid in 30 day month")



elif month ==  1 or month == 3 or month == 5 or month == 7  or month == 8 or month == 10 or month == 12:
    print("valid 31 day month")
    if 1 <= day <= 31:
             print("day is invalid")
    else: 
        print("day is valid in 31 day month")



elif  month == 2:
    if 1 <= day <= 28:
             print("day is invalid")
    elif day ==  29 and isLeapYear(year):
        print("valid leap year")



elif month > 12:
    print("bad month")"
"""
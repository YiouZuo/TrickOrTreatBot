import RPi.GPIO as GPIO
import time

def turn_servo():

    servoPIN = 14
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servoPIN, GPIO.OUT)

    p = GPIO.PWM(servoPIN, 50) # GPIO 14 for PWM with 50Hz
    p.start(7) # Initialization
    time.sleep(0.1)
    try:
        p.ChangeDutyCycle(12)
        time.sleep(3)
        p.ChangeDutyCycle(7)
        time.sleep(0.5)
        p.ChangeDutyCycle(5.5)
        time.sleep(0.3)
        p.ChangeDutyCycle(4)
        time.sleep(0.3)
        p.ChangeDutyCycle(3)
        time.sleep(0.3)
        p.ChangeDutyCycle(5)
        time.sleep(0.3)
        p.ChangeDutyCycle(7)
        time.sleep(0.1)
    except KeyboardInterrupt:
      p.stop()
      GPIO.cleanup()

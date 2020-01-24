import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) # use command pinout to find GPIO number
GPIO.setwarnings(False) # mute warnings
led_input = 13
GPIO.setup(led_input,GPIO.OUT)
print("LED on")
GPIO.output(led_input,GPIO.HIGH)
time.sleep(5)
print("LED off")
GPIO.output(led_input,GPIO.LOW)

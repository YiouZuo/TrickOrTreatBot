import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import time
from turn_servo import turn_servo


def push_button():

    # set up button
    button_input = 26
    GPIO.setwarnings(False) # Set to False to ignore warning for now
    GPIO.setmode(GPIO.BCM) # Use physical pin numbering
    GPIO.setup(button_input, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    # set up LED light for ready to push indication
    led_input = 13
    GPIO.setup(led_input, GPIO.OUT)
    GPIO.output(led_input, GPIO.HIGH)

    # turn off the light when servo is working
    input_state = GPIO.input(button_input)
    if input_state == False:
        # print("Button Pressed")
        GPIO.output(led_input, GPIO.LOW)
        turn_servo()
        time.sleep(0.5)

if __name__ == "__main__":
    while True:
        push_button()


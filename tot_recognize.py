import random
import time
from turn_servo import turn_servo
import speech_recognition as sr
from push_button import push_button
import RPi.GPIO as GPIO


def recognize_speech_from_mic(recognizer, microphone):
    """Transcribe speech from recorded from `microphone`.

    Returns a dictionary with three keys:
    "success": a boolean indicating whether or not the API request was
               successful
    "error":   `None` if no error occured, otherwise a string containing
               an error message if the API could not be reached or
               speech was unrecognizable
    "transcription": `None` if speech could not be transcribed,
               otherwise a string containing the transcribed text
    """
    # check that recognizer and microphone arguments are appropriate type
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    # adjust the recognizer sensitivity to ambient noise and record audio
    # from the microphone
    print("A moment of silence, please...")
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        # recognizer.energy_threshold = 4000
        print("Set minimum energy threshold to {}".format(recognizer.energy_threshold))

        # set up LED light for indication
        led_input = 13
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(led_input, GPIO.OUT)
        GPIO.output(led_input, GPIO.HIGH)
        time.sleep(1)

        audio = recognizer.listen(source, phrase_time_limit=3)
        GPIO.output(led_input, GPIO.LOW)
        print("Got it! Now to recognize it...")
        GPIO.cleanup()

    # set up the response object
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    # try recognizing the speech in the recording
    # if a RequestError or UnknownValueError exception is caught,
    #     update the response object accordingly
    try:
        response["transcription"] = recognizer.recognize_google(audio, language="en-US")
    except sr.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        # speech was unintelligible
        response["error"] = "Unable to recognize speech"

    return response


if __name__ == "__main__":

    # create recognizer and mic instances
    recognizer = sr.Recognizer()
    print("recognizer instance created")
    microphone = sr.Microphone(device_index=2)
    print("mic instance created")

    while True:

        # give candy, aka turn servo when heard "trick or treat"
        tot = recognize_speech_from_mic(recognizer, microphone)
        # if tot["transcription"].lower() == 'trick or treat': # for strict matching, you can also pass a list of possible matchings
        if tot["transcription"]:
            turn_servo()

        # in reality, not always successfully recognized, hence set to turn servo no matter what
        if not tot["success"]:
            turn_servo()

        if tot["error"]:
            print("ERROR: {}".format(tot["error"]))
            turn_servo()


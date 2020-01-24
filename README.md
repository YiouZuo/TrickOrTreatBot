# TrickOrTreatBot
Trick-or-Treat Pumpkin robot

It all started when I was talking to my 4-year-old son in early October, 2019 about the coming Halloween. 
We were talking about robots and candies, and it struck me -- wouldn't it be nice to have a robot that 
hands you candy when you say "Trick-Or-Treat"?!
I talked to my colleage Paul Davis who is quite crafty and googled a whole bunch.
Long story short, we came up with this Pumpkin Robot. 
![robot](https://github.com/YiouZuo/TrickOrTreatBot/blob/master/TOT_robot.jpg)

## Hardware
Since I wanted speech recognition, I chose RaspberryPi, and an external microphone. 
In the end, the speech recognition took longer than most children's patience allowed, 
I turned it off and just used a push button. 
So RPi could be an overkill.

The candy dispenser mechanism is inspired by the [Jelly Bean BeanBoozled Mystery Bean Jelly Bean Dispenser](https://www.amazon.com/Jelly-Belly-BeanBoozled-Dispenser-Assorted/dp/B0106HIT18/ref=asc_df_B0106HIT18/?tag=hyprod-20&linkCode=df0&hvadid=312061073410&hvpos=1o6&hvnetw=g&hvrand=2422447797311280400&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9032078&hvtargid=pla-356038182226&psc=1&tag=&ref=&adgrpid=58872081541&hvpone=&hvptwo=&hvadid=312061073410&hvpos=1o6&hvnetw=g&hvrand=2422447797311280400&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9032078&hvtargid=pla-356038182226).
We used a cut-off juice box as a bowl to hold candies, a PVC pipe to push up the candy, and a servo to pull the PVC pipe. 
When the bowl is full of candies, the servo doesn't have enough torqque, 
so we added a short piece of rubber band just to help it out.

![inside pic](https://github.com/YiouZuo/TrickOrTreatBot/blob/master/TOT_robot_inside.jpg)

## Software
You'll need the `GPIO` package, and the `pinout` command will show you the GPIO numbers on your RPi.

### Servo
Use `turn_servo.py` to test your servo. I played around with the range, pause time and steps to get what I want.
For more detail on how to set up a servo on RPi, see [this article](https://tutorials-raspberrypi.com/raspberry-pi-servo-motor-control/).

### Button
See `push_button.py`. When pushed, the button will trigger the servo to lift the PVC pipe and 
push up a (occasionally 2) piece of candy.
See [this article](https://raspberrypihq.com/use-a-push-button-with-raspberry-pi-gpio/) for how to connect your button.

### LED light
This is an optional add on, though proved to be quite practical during the Halloween night. 
It turns the light on when the servo is ready. 
Use `test_led.py`to test your light. 

### Speech recognition
I followed [this article](https://realpython.com/python-speech-recognition/) to set up the "Trick or Treat" recognition. 
If you see error messages from ALSA, you can safely ignore it according to [this article](https://github.com/Uberi/speech_recognition#on-ubuntudebian-i-get-annoying-output-in-the-terminal-saying-things-like-bt_audio_service_open--connection-refused-and-various-others).
In a quiet room, when I speak loud and clear, it works well. 
However, most of the time, it doesn't get it right. 
I tried to loose the matching to a list of options, but eventually decided to set it such that whatever you say, 
it will trigger the servo. 
See `tot_recognize.py` for my code.

On the Halloween night, after a few kids, I had to unplugged the mic because most kids, though interested in the robot, 
are not interested enough to wait for a couple of seconds for their candy (so many houses to hit!). 
Pushing a button and see the candy coming up was sufficiently intriguing.

### Auto run on RPi starts
I used `crontab -e` and added the `push_button.py` to run automatically when RPi starts.




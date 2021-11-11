from gpiozero import Button
from subprocess import check_call

# GPIO   2, 4, 17 and 10
button1 = Button(2, hold_time=2)
button2 = Button(4, bounce_time=0.1)
button3 = Button(17, bounce_time=0.1)
button4 = Button(10, bounce_time=0.1)


def powerButton():
    print("shutting down")
    check_call(['sudo', 'poweroff'])


def pauseButton():
    print("pause button pressed")


def backButton():
    print("back button pressed")


def forwardButton():
    print(" forward button pressed")


# Mapping functions to button presses
button1.when_pressed = powerButton
button2.when_pressed = pauseButton
button3.when_pressed = backButton
button4.when_pressed = forwardButton

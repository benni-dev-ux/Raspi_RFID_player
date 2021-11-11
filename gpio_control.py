from gpiozero import Button

# GPIO   2, 4, 17 and 10
button1 = Button(2, bounce_time=0.5)
button2 = Button(4, bounce_time=0.5)
button3 = Button(17, bounce_time=0.5)
button4 = Button(10, bounce_time=0.5)

button1.when_pressed = print("button1 pressed")
button2.when_pressed = print("button2 pressed")
button3.when_pressed = print("button3 pressed")
button4.when_pressed = print("button4 pressed")

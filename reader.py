from subprocess import check_call

from gpiozero import Button

import media_player


def power_button():
    print("\n Shutting down the Device")
    check_call(['sudo', 'poweroff'])


def pause_button():
    print("\n Pause button pressed")

    try:
        playerOB
    except NameError:
        print("\n No music player defined")
    else:
        playerOB.play_pause()


def back_button():
    print("\n Stopping all Media")
    media_player.stopAllMedia()


def forward_button():
    print("\n forward button pressed")


def main():
    print("\n RFID Player Started")
    global playerOB

    # GPIO   3, 4, 17 and 10
    button1 = Button(3, hold_time=2)
    button2 = Button(4, bounce_time=0.1)
    button3 = Button(17, bounce_time=0.1)
    button4 = Button(10, bounce_time=0.1)

    # Mapping functions to button presses
    button1.when_pressed = power_button
    button2.when_pressed = back_button
    button3.when_pressed = pause_button
    button4.when_pressed = forward_button

    # Main Loop of the App: Constantly checking for new  RFID input
    while True:
        code = check_for_input()
        # Check if found code occurs in media list
        for media in media_list:
            if media[1] == code:
                print("Playing " + media[0] + " at " + media[2])
                playerOB = media_player.play_media(media[2])


# Testfiles
video1 = ["testvideo", 6267256,
          "/home/pi/Raspi_RFID_player/assets/testvideo.mp4"]
audio1 = ["testaudio", 6268576,
          "/home/pi/Raspi_RFID_player/assets/testaudio.mp3"]

media_list = [video1, audio1]


def check_for_input():
    code = input('\n Scan RFID tag to Play Media \n')
    # Strip first three Characters to avoid escape characters
    code = code[3:]
    # Cast to int
    code = int(code)
    return code


if __name__ == "__main__":
    main()

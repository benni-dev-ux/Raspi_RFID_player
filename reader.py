from typing import Match
from gpiozero import Button
from subprocess import check_call
import media_player
import logging




def powerButton():
    print("shutting down")
    check_call(['sudo', 'poweroff'])


def pauseButton():
    print("pause button pressed")
    
    try:
        playerOB
    except PlayerUnedfined:
        print ("No music player defined")
    else:
        playerOB.play_pause()
 


def backButton():
    print("Stopping all Media")
    media_player.stopAllMedia()


def forwardButton():
    print(" forward button pressed")


def main():
    print("Setting up Button Controls")
    global playerOB
    
    # GPIO   3, 4, 17 and 10
    button1 = Button(3, hold_time=2)
    button2 = Button(4, bounce_time=0.1)
    button3 = Button(17, bounce_time=0.1)
    button4 = Button(10, bounce_time=0.1)
        
    # Mapping functions to button presses
    button1.when_pressed = powerButton
    button2.when_pressed = backButton
    button3.when_pressed = pauseButton
    button4.when_pressed = forwardButton
    
    
    # Main Loop of the App: Constantly checking for new  RFID input
    while(True):
        code = check_for_input()
          # Check if found code occurs in media list
        for media in media_list:
            if(media[1] == code):
               
                print("Playing " + media[0] + " at " + media[2])
                playerOB = media_player.play_media(media[2])




# Testfiles
video1 = ["testvideo", 6267256, "./assets/testvideo.mp4"]
audio1 = ["testaudio", 6268576, "./assets/testaudio.mp3"]


media_list = []

media_list.append(video1)
media_list.append(audio1)


def check_for_RFIDMatch(code, media_list):
    
    # Check if found code occurs in media list
    for media in media_list:
        if(media[1] == code):
           
            print("Playing " + media[0] + " at " + media[2])
            playerOB = media_player.play_media(media[2])


def check_for_input():
    code = input('Start by scanning an RFID tag')
    # Strip first three Characters to avoid escape characters
    code = code[3:]
    # Cast to int
    code = int(code)
    return code


    
if __name__=="__main__":
    main()

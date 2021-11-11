from typing import Match
import media_player
import logging


# Testfiles
video1 = ["testvideo", 6267256, "./assets/testvideo.mp4"]
audio1 = ["testaudio", 6268576, "./assets/testaudio.mp3"]


media_list = []


def check_for_RFIDMatch(code, media_list):
    # Check if found code occurs in media list
    for media in media_list:
        if(media[1] == code):
            logging.debug("Playing" + media[0] + " at " + media[2])
            media_player.play_media(media[2])


def check_for_input():
    code = input('Scan an RFID tag')
    # Strip first three Characters to avoid escape characters
    code = code[3:]
    # Cast to int
    code = int(code)
    return code


# Main Loop of the App: Constantly checking for new  RFID input
while(True):
    code = check_for_input()
    check_for_RFIDMatch(code, media_list)

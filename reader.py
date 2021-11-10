from typing import Match
import video_player


video1 = ["testvideo", 6267256, "./assets/testvideo.mp4"]
audio1 = ["testaudio", 6268576, "./assets/testaudio.mp3"]


media_list = []

media_list.append(video1)
media_list.append(audio1)

# read and sanitize input
code = input('Enter your input:')
code = code[3:]
code = int(code)

print("Found RFID tag: ")


for med in media_list:
    if(med[1] == code):
        print("playing" + med[0] + " at " + med[2])
        video_player.playmovie(med[2])

import subprocess
import os
import logging


def is_playing():
    """Check if OMX Player is playing a Video/Audio file 
    (True if at least 2 OMX Processes)"""

    processname = 'omxplayer'
    tmp = os.popen("ps -Af").read()
    proccesscount = tmp.count(processname)

    is_playing = False

    if (proccesscount >= 1):
        is_playing = True

    return is_playing


def play_media(filename):

    global myprocess

    if is_playing():
        logging.debug("Cancelling currently playing video/audio")

        # Kill existing OMX Processes
        command1 = "sudo killall -s 9 omxplayer.bin"
        os.system(command1)

    # starting OMXPlayer subprocess with video or audio file
    myprocess = subprocess.Popen(['omxplayer', filename], stdin=subprocess.PIPE,
                                 stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)

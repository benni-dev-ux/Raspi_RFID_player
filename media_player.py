import os

from omxplayer.player import OMXPlayer


def is_playing():
    """Check if OMX Player is playing a Video/Audio file
    (True if at least 2 OMX Processes)"""

    processname = 'omxplayer'
    tmp = os.popen("ps -Af").read()
    proccesscount = tmp.count(processname)

    is_currently_playing = False

    if proccesscount >= 1:
        is_currently_playing = True

    return is_currently_playing


def play_media(filename):
    """ Plays file (audio or video) in OMXPlayer"""
    if is_playing():
        print("Cancelling currently playing video/audio")

        # Kill existing OMX Processes
        command1 = "sudo killall -s 9 omxplayer.bin"
        os.system(command1)

    # starting OMXPlayer subprocess with video or audio file
    player = OMXPlayer(filename, dbus_name='org.mpris.MediaPlayer2.omxplayer1')
    # myprocess = subprocess.Popen(['omxplayer', filename], stdin=subprocess.PIPE,
    #                            stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)
    # time.sleep(2)
    return player


def stopAllMedia():
    """Kills all existing OMX processes"""

    command1 = "sudo killall -s 9 omxplayer.bin"
    os.system(command1)

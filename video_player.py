import subprocess


def playmovie(filename):

    myprocess = subprocess.Popen(['omxplayer', directory + filename], stdin=subprocess.PIPE,
                                 stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)

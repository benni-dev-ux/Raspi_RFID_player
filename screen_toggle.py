# function derived from:
# https://www.youtube.com/watch?v=lETqSCimcyM

from subprocess import run


def toggleDisplay(active):
    if(active):
        run('vgencmd display_power 1', shell=True)
    else:
        run('vgencmd display_power 0', shell=True)

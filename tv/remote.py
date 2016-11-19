# -*- coding: utf-8 -*-

from subprocess import check_call, CalledProcessError

OMXCMDS = {
        'play':        "p",
        'volume_down': "-",
        'volume_up':   "+",
        'seek_fwd':    "$'\e'[C",
        'seek_back':   "$'\e'[D"
    }

MPVCMDS = {
        'play':        "keypress p\n",
        'volume_down': "keypress 9\n",
        'volume_up':   "keypress 0\n",
        'seek_fwd':    "seek 30\n",
        'seek_back':   "seek -30\n"
    }

class Remote(object):

    def __init__(self, player='MPV', fifo='/tmp/tv.fifo'):
        self.player = player
        self.fifo = fifo
        self.cmds = None
        self.bin = None

        if self.player == 'OMX':
            self.cmds = OMXCMDS
            self.bin = "/usr/local/bin/omx.sh"
        elif self.player == 'MPV':
            self.cmds = MPVCMDS
            self.bin = "/usr/local/bin/mpv.sh"

    def send(self, cmd):
        with open(self.fifo, 'w') as fifo:
            fifo.write(cmd)

    def pause_resume(self):
        self.send(self.cmds['play'])

    def stop(self):
        check_call([self.bin, 'stop'])

    def volume_down(self):
        self.send(self.cmds['volume_down'])

    def volume_up(self):
        self.send(self.cmds['volume_up'])

    def seek_fwd(self):
        self.send(self.cmds['seek_fwd'])

    def seek_back(self):
        self.send(self.cmds['seek_back'])

    def load(self, uri):
        check_call([self.bin, 'stop'])
        check_call([self.bin, 'start', '%s' % uri])

    def status(self):
        try:
            check_call([self.bin, 'status'])
        except CalledProcessError:
            return False
        else:
            return True

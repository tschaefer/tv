#!/bin/bash

MPVPLAYER="/usr/local/bin/mpv"
MPVBIN=$(basename $MPVPLAYER)
MPVARGS=""
MPVFIFO="/tmp/tv.fifo"
MPVINPUT="--input-file=${MPVFIFO}"

case "$1" in
    start)
        pgrep $MPVBIN >/dev/null 2>&1
        if [ $? -eq 0 ]; then
            exit 1
        fi
        if [ ! -p $MPVFIFO ]; then
            mkfifo $MPVFIFO
        fi
        $MPVPLAYER $MPVARGS $MPVINPUT $2 >/dev/null 2>&1 &
        echo -n "" > $MPVFIFO
        ;;
     stop)
        pgrep $MPVBIN >/dev/null 2>&1
        if [ $? -eq 0 ]; then
            kill -n 9 $(pgrep $MPVBIN) >/dev/null 2>&1
        fi
        rm -f $MPVFIFO >/dev/null 2>&1
        ;;
     status)
        pgrep $MPVBIN >/dev/null 2>&1
        exit $?
        ;;
     *)
        exit 1
        ;;
esac

exit 0

#!/bin/bash

OMXPLAYER="/usr/bin/omxplayer.bin"
OMXBIN=$(basename $OMXPLAYER)
OMXARGS="-o hdmi"
OMXENV="/opt/vc/lib:/usr/lib/omxplayer"
OMXFIFO="/tmp/tv.fifo"
OMXVERSION=$(LD_LIBRARY_PATH=$OMXENV $OMXPLAYER --version | \
    awk '/Version/ { print $3 }')

case "$1" in
    start)
        pgrep $OMXBIN >/dev/null 2>&1
        if [ $? -eq 0 ]; then
            exit 1
        fi
        if [ ! -p $OMXFIFO ]; then
            mkfifo $OMXFIFO
        fi
        LD_LIBRARY_PATH=$OMXENV \
            $OMXPLAYER $OMXARGS $2 < $OMXFIFO >/dev/null 2>&1 &
        echo -n "" > $OMXFIFO
        ;;
     stop)
         kill -9 $(pgrep $OMXBIN) >/dev/null 2>&1
         rm -f $OMXFIFO >/dev/null 2>&1
         ;;
     status)
         pgrep $OMXBIN >/dev/null 2>&1
         exit $?
         ;;
     version)
         echo "omxplayer $OMXVERSION"
         ;;
     *)
        exit 1
        ;;
esac

exit 0

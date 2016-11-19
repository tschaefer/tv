# tv

REST API service for the awesome OMXPlayer and MPV.

## Installation

Install package, scripts and systemd unit file.

    $ sudo cp omx.sh /usr/local/bin/omx.sh
    $ sudo cp mpv.sh /usr/local/bin/mpv.sh
    $ sudo cp tv.service /etc/systemd/system/tv.service
    $ sudo systemctl enable tv.service
    $ sudo python setup.py install

## Usage

Start REST API service.

    $ sudo systemctl start tv.service

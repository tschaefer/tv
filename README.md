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

## REST API

Documentation is subdivided in REST API endpoints. Every endpoint is prefixed by
following base URL:

    /tv/api/v1.0/

Every endpoint allows only `POST` requests and has one mandatory field `action`
and one optional field `data`.

The service will answer with a suitable HTTP status code and a JSON fragment.

Response *ok*

    {
      "action": "start",
      "endpoint": "playback",
      "player": "omxplayer dfea8c9\n"
    }

Response *error*

    {
      "endpoint": "playback",
      "error": "bad action",
      "player": "omxplayer dfea8c9\n"
    }

### Playback

| Action    | Data               | Description                       |
| --------- | ------------------ | --------------------------------- |
| **start** | URI to media file  | Start player and play media file. |
| **stop**  | *none*             | Stop playback and player.         |
| **play**  | *none*             | Play / pause playback.            |
| **pause** | *none*             | Play / pause playback             |

#### Example

    $ curl -i -H "Content-Type: application/json" -X POST -d '{"action": "start", "data": "http://tinyurl.com/hv5y29q"}' http://localhost:8090/tv/api/v1.0/playback
    $ curl -i -H "Content-Type: application/json" -X POST -d '{"action": "stop" }' http://localhost:8090/tv/api/v1.0/playback
    $ curl -i -H "Content-Type: application/json" -X POST -d '{"action": "play" }' http://localhost:8090/tv/api/v1.0/playback
    $ curl -i -H "Content-Type: application/json" -X POST -d '{"action": "pause" }' http://localhost:8090/tv/api/v1.0/playback

### Volume

| Action   | Data   | Description      |
| -------- | ------ | ---------------- |
| **up**   | *none* | Increase volume. |
| **down** | *none* | Decrease volume. |

#### Example

    $ curl -i -H "Content-Type: application/json" -X POST -d '{"action": "up" }' http://localhost:8090/tv/api/v1.0/volume
    $ curl -i -H "Content-Type: application/json" -X POST -d '{"action": "down" }' http://localhost:8090/tv/api/v1.0/volume

### Seek

| Action   | Data   | Description    |
| -------- | ------ | -------------- |
| **fwd**  | *none* | Seek forward.  |
| **back** | *none* | Seek backword. |

#### Example

    $ curl -i -H "Content-Type: application/json" -X POST -d '{"action": "fwd" }' http://localhost:8090/tv/api/v1.0/seek
    $ curl -i -H "Content-Type: application/json" -X POST -d '{"action": "back" }' http://localhost:8090/tv/api/v1.0/seek

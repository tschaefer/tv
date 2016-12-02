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
and two further fields `data` and `options`.

Request

    {
      "action": "start",
      "endpoint": "playback",
      "options": "local",
      "data": "https://www.youtube.com/watch?v=IAISUDbjXj0"
    }

The service will answer with a suitable HTTP status code and a JSON fragment.

Response *ok* 202

    {
      "action": "start",
      "endpoint": "playback",
      "player": "omxplayer dfea8c9\n"
    }

Response *error* 404

    {
      "endpoint": "playback",
      "error": "bad action",
      "player": "omxplayer dfea8c9\n"
    }

### Playback

| Action    | Data               | Options       | Description                       |
| --------- | ------------------ | ------------- | --------------------------------- |
| **start** | URI to media file  | live or local | Start player and play media file. |
| **stop**  | *none*             | *none*        | Stop playback and player.         |
| **play**  | *none*             | *none*        | Play / pause playback.            |
| **pause** | *none*             | *none*        | Play / pause playback             |

`live` sets the OMXPlayer options `--live --timeout=20 --adev hdmi`. `local`
sets the OMXPlayer options `--adev hdmi`.

#### Example

    $ curl -i -H "Content-Type: application/json" -X POST -d '{"action": "start", "data": "http://tinyurl.com/hv5y29q"}' http://localhost:8090/tv/api/v1.0/playback
    $ curl -i -H "Content-Type: application/json" -X POST -d '{"action": "stop" }' http://localhost:8090/tv/api/v1.0/playback
    $ curl -i -H "Content-Type: application/json" -X POST -d '{"action": "play" }' http://localhost:8090/tv/api/v1.0/playback
    $ curl -i -H "Content-Type: application/json" -X POST -d '{"action": "pause" }' http://localhost:8090/tv/api/v1.0/playback

### Volume

| Action   | Data   | Options | Description      |
| -------- | ------ | ------- | ---------------- |
| **up**   | *none* | *none*  | Increase volume. |
| **down** | *none* | *none*  | Decrease volume. |

#### Example

    $ curl -i -H "Content-Type: application/json" -X POST -d '{"action": "up" }' http://localhost:8090/tv/api/v1.0/volume
    $ curl -i -H "Content-Type: application/json" -X POST -d '{"action": "down" }' http://localhost:8090/tv/api/v1.0/volume

### Seek

| Action   | Data   | Options | Description    |
| -------- | ------ | ------- | -------------- |
| **fwd**  | *none* | *none*  | Seek forward.  |
| **back** | *none* | *none*  | Seek backword. |

#### Example

    $ curl -i -H "Content-Type: application/json" -X POST -d '{"action": "fwd" }' http://localhost:8090/tv/api/v1.0/seek
    $ curl -i -H "Content-Type: application/json" -X POST -d '{"action": "back" }' http://localhost:8090/tv/api/v1.0/seek

# -*- coding: utf-8 -*-

from flask import Flask, jsonify, make_response
from flask_restful import Api, Resource, reqparse
from remote import Remote

app = Flask(__name__)
api = Api(app)
remote = Remote()

class Api(object):

    def __init__(self):
        self.endpoint = ""
        self.action = ""

    def make_response_ok(self, code):
        response = {
            'player':   remote.player_version(),
            'endpoint': self.endpoint,
            'action':   self.action
        }
        return make_response(jsonify(response), code)

    def make_response_error(self, msg, code):
        response = {
            'player':   remote.player_version(),
            'endpoint': self.endpoint,
            'error':    msg
        }
        return make_response(jsonify(response), code)

class Playback(Api, Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('action', type=str, default='',
                                   location='json')
        self.reqparse.add_argument('data', type=str, default='',
                                   location='json')
        super(Playback, self).__init__()

    def post(self):
        self.endpoint = 'playback'
        args = self.reqparse.parse_args()
        self.action = args['action']

        if self.action == 'play':
            if not remote.player_status():
                return self.make_response_error('player not running', 406)
            remote.playback_play()
        elif self.action == 'pause':
            if not remote.player_status():
                return self.make_response_error('player not running', 406)
            remote.playback_pause()
        elif self.action == 'stop':
            remote.playback_stop()
        elif self.action == 'start':
            data = args['data']
            if not data:
                return self.make_response_error('missing data', 400)
            remote.playback_start(args['data'])
        else:
            return self.make_response_error('bad action', 400)

        return self.make_response_ok(202)


class Volume(Api, Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('action', type=str, default='',
                                   location='json')
        self.reqparse.add_argument('data', type=str, default='',
                                   location='json')
        super(Volume, self).__init__()

    def post(self):
        self.endpoint = 'volume'
        args = self.reqparse.parse_args()
        self.action = args['action']

        if self.action == 'up':
            remote.volume_up()
        elif self.action == 'down':
            remote.volume_down()
        else:
            return self.make_response_error('bad action', 400)

        return self.make_response_ok(202)


class Seek(Api, Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('action', type=str, default='',
                                   location='json')
        self.reqparse.add_argument('data', type=str, default='',
                                   location='json')
        super(Seek, self).__init__()

    def post(self):
        self.endpoint = 'seek'
        args = self.reqparse.parse_args()
        self.action = args['action']

        if self.action == 'fwd':
            remote.seek_fwd()
        elif self.action == 'down':
            remote.seek_back()
        else:
            return self.make_response_error('bad action', 400)

        return self.make_response_ok(202)


api.add_resource(Playback, '/tv/api/v1.0/playback', endpoint='playback')
api.add_resource(Volume, '/tv/api/v1.0/volume', endpoint='volume')
api.add_resource(Seek, '/tv/api/v1.0/seek', endpoint='seek')


class Service(object):

    def __init__(self, host=None, port=None):
        self.host = host
        self.port = port

    def run(self):
        app.run(host=self.host, port=self.port,
                debug=True, threaded=True)

# -*- coding: utf-8 -*-

from flask import Flask, jsonify, request, make_response, abort
from remote import Remote

app = Flask(__name__)

remote = Remote()

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/', methods=['GET'])
def omx():
    return "OMXPlayer RESTFull API."

@app.route('/omx/api/v1.0/load', methods=['POST'])
def load():
    if not request.json:
        abort(400)
    if 'uri' not in request.json:
        abort(400)

    uri = request.json['uri']
    remote.load(uri)

    return jsonify({'load': uri}), 201

@app.route('/omx/api/v1.0/playback', methods=['POST'])
def playback():
    if not request.json:
        abort(400)
    if not remote.status():
        abort(404)
    if 'action' not in request.json:
        abort(400)

    action = request.json['action']
    if action == 'resume' or action == 'pause':
        remote.pause_resume()
    elif action == 'stop':
        remote.stop()
    else:
        abort(400)

    return jsonify({'playback':  action}), 201

@app.route('/omx/api/v1.0/volume', methods=['POST'])
def volume():
    if not request.json:
        abort(400)
    if not remote.status():
        abort(404)
    if 'action' not in request.json:
        abort(400)

    action = request.json['action']
    if action == 'up':
        remote.volume_up()
    elif action == 'down':
        remote.volume_down()
    else:
        abort(400)

    return jsonify({'volume':  action}), 201

@app.route('/omx/api/v1.0/seek', methods=['POST'])
def seek():
    if not request.json:
        abort(400)
    if not remote.status():
        abort(404)
    if 'action' not in request.json:
        abort(400)

    action = request.json['action']
    if action == 'fwd':
        remote.seek_fwd()
    elif action == 'back':
        remote.seek_back()
    else:
        abort(400)

    return jsonify({'seek':  action}), 201

class Service(object):

    def __init__(self, host=None, port=None):
        self.host = host
        self.port = port

    def run(self):
        app.run(host=self.host, port=self.port,
                debug=True, threaded=True)

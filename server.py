# MoodTrackr : Server to track your mood.
# Authors :  Korhan Akcura

import json
import requests
import logging
from models.emotion import emotion
from models.suggestion import suggestion

from logging.handlers import RotatingFileHandler

from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

app = Flask(__name__, static_url_path='')
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# Response bots.
emotion_bot = emotion.emotion()
suggestion_bot = suggestion.suggestion()

@app.route("/", methods=['GET', 'POST'])
def root(): 
	return app.send_static_file('index.html')

@app.route('/analize', methods=['POST'])
def analize():

	text_to_analyze = request.get_data()

	emotion_params = emotion_bot.predict(text_to_analyze)
	url = suggestion_bot.suggest(emotion_params);

	response = {
		"response"   : "You are probably feeling " + emotion_params['emotion'] +".<br/>We suggest you to watch this video. :)",
		"emotion"    : emotion_params['emotion'],
		"url" : url
	}

	return jsonify(response)

if __name__ == '__main__':
	handler = RotatingFileHandler('server.log', maxBytes=10000, backupCount=1)
	handler.setLevel(logging.INFO)
	app.logger.addHandler(handler)
	app.run(host="localhost",port=5000)


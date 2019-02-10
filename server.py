# MoodTrackr : Server to track your mood.
# Authors :  Korhan Akcura

import json
import requests
import logging
from models.emotion import emotion

from logging.handlers import RotatingFileHandler

from flask import Flask, jsonify, request

app = Flask(__name__, static_url_path='')

# Response bots.
emotion_bot = emotion.emotion()

@app.route("/", methods=['GET', 'POST'])
def root(): 
	return app.send_static_file('index.html')

@app.route('/analize', methods=['POST'])
def analize():

	text_to_analyze = request.get_data()

	emotion = emotion_bot.predict(text_to_analyze)

	return emotion

if __name__ == '__main__':
	handler = RotatingFileHandler('server.log', maxBytes=10000, backupCount=1)
	handler.setLevel(logging.INFO)
	app.logger.addHandler(handler)
	app.run(host="127.0.0.1",port=5000)


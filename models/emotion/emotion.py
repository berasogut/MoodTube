#----------------------------------------------------------------------
#  emotion.py
#
# Predict emotion from a text input.
# Authors :  Korhan Akcura
#----------------------------------------------------------------------
from random import randint
from thesaurus import Word
import itertools
import json
import requests
import string

WATSON_API_KEY = "Put yours here."
WATSON_URL = "Put yours here."

class emotion:
	def __init__(self):
		self.emotions= ["happy", "sad", "angry", "excited","fearful"]
		emotion_properties = [Word(self.emotions[0]),Word(self.emotions[1]),Word(self.emotions[2]),Word(self.emotions[3]),Word(self.emotions[4])]
		self.happy_synonyms = list(itertools.chain.from_iterable(emotion_properties[0].synonyms('all')))
		self.happy_antonym = emotion_properties[0].antonyms()[0]
		self.sad_synonyms = list(itertools.chain.from_iterable(emotion_properties[1].synonyms('all')))
		self.sad_antonym = emotion_properties[1].antonyms()[0]
		self.angry_synonyms = list(itertools.chain.from_iterable(emotion_properties[2].synonyms('all')))
		self.angry_antonym = emotion_properties[2].antonyms()[0]
		self.excited_synonyms = list(itertools.chain.from_iterable(emotion_properties[3].synonyms('all')))
		self.excited_antonym = emotion_properties[3].antonyms()[0]
		self.fearful_synonyms = list(itertools.chain.from_iterable(emotion_properties[4].synonyms('all')))
		self.fearful_antonym = emotion_properties[4].antonyms()[0]


	#----------------------------------------------------------------------
	#  Predict the emotion of a text as happy, sad or natural.
	#----------------------------------------------------------------------
	def predict(self,str):

		#prediction = {"emotion": "natural", "confidence": 100}
		cur_emotion = False
		res_emotion = False


		response = self.analyze_tone(str)


		if response:

			tones = json.loads(response)['document_tone']['tones']
			for tone in tones:
				cur_emotion=self.match_synonym(tone['tone_id'])
				if cur_emotion:
					break
				else:
					res_emotion = tone['tone_id']

		if not cur_emotion:
			cur_emotion=self.match_synonym(str.translate(None, string.punctuation))

		if not cur_emotion:
			cur_emotion=res_emotion

		if not cur_emotion:
			cur_emotion="natural"

		if cur_emotion not in ["happy", "sad", "angry", "excited","fearful"]:
			cur_emotion=Word(cur_emotion).synonyms(partOfSpeech='adj')[0]
			if not cur_emotion:
				cur_emotion = res_emotion
			if cur_emotion == 'joy':
				cur_emotion += "ful"
			#if cur_emotion == 'unsettled':
			#	cur_emotion = "sad"	

		cur_antonym = self.match_antonym(cur_emotion)

		return {"emotion": cur_emotion, "antonym": cur_antonym}	


	def match_synonym(self,text):
		prediction = {"emotion": False}

		# Lowercase and break string into individual words
		potential_emotion_words = text.lower().split()

		# Detect if Happy
		if any((s in self.happy_synonyms or s == self.emotions[0]) for s in potential_emotion_words):
			prediction["emotion"] = self.emotions[0]
		# Detect if Sad
		elif any((s in self.sad_synonyms or s == self.emotions[1]) for s in potential_emotion_words):
			prediction["emotion"] = self.emotions[1]
		elif any((s in self.angry_synonyms or s == self.emotions[2]) for s in potential_emotion_words):
			prediction["emotion"] = self.emotions[2]
		elif any((s in self.excited_synonyms or s == self.emotions[3]) for s in potential_emotion_words):
			prediction["emotion"] = self.emotions[3]
		elif any((s in self.fearful_synonyms or s == self.emotions[4]) for s in potential_emotion_words):
			prediction["emotion"] = self.emotions[4]		

		return prediction["emotion"]

	def match_antonym(self,text):
		prediction = {"antonym": "natural"}

		# Detect if Happy
		if any(s in self.happy_antonym for s in text):
			prediction["antonym"] = self.emotions[0]
		# Detect if Sad
		elif any(s in self.sad_antonym for s in text):
			prediction["antonym"] = self.emotions[1]
		elif any(s in self.angry_antonym for s in text):
			prediction["antonym"] = self.emotions[2]
		elif any(s in self.excited_antonym for s in text):
			prediction["antonym"] = self.emotions[3]
		elif any(s in self.fearful_antonym for s in text):
			prediction["antonym"] = self.emotions[4]		

		return prediction["antonym"]

	def analyze_tone(self,text):
		headers = {"content-type": "text/plain"}
		data = text
		try:
			r = requests.post(WATSON_URL, auth=('apikey', WATSON_API_KEY),headers = headers,
			 data=data)
			return r.text
		except:
			return False
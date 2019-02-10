#----------------------------------------------------------------------
#  suggestion.py
#
# Make YouTube video suggestions based on emotion.
# Authors :  Korhan Akcura
#----------------------------------------------------------------------
import requests
from bs4 import BeautifulSoup
from random import randint

class suggestion:
	def __init__(self):
		self.watch_url = '/watch?v='
		self.full_embed_url = 'https://www.youtube.com/embed/'
		
	#----------------------------------------------------------------------
	#  Suggest a become an emotion video.
	#----------------------------------------------------------------------
	def suggest(self,emotion_params):
		if emotion_params['emotion'] in ["sad", "angry", "excited","fearful"]:
			url = 'https://www.youtube.com/results?search_query=%22be+'+emotion_params['antonym']+'%22';
			print(url)
		else:
			url = 'https://www.youtube.com/results?search_query=%22I+am+'+emotion_params['emotion']+'%22';
			print(url)
		response = requests.get(url)
		# parse html
		page = str(BeautifulSoup(response.content.decode('utf-8','ignore')))

		while True:
			vidId, n = self.getVideoID(page)
			page = page[n:]
			if vidId:
				if randint(0, 3) == 1:
					break
				if randint(0, 1) == 1:
					return ""
					break
			else:
				break

		print(self.full_embed_url + vidId)
		# Check if video is avaliable.
		#response = requests.get(self.full_embed_url + vidId + "?autoplay=1")
		#page = str(BeautifulSoup(response.content.decode('utf-8','ignore')))
		#if page.find('div class="ytp-error') or resp.status_code == 404:
		#	return ""

		return self.full_embed_url + vidId + "?autoplay=1"

	def getVideoID(self,page):
		start_link = page.find('href="'+self.watch_url)
		if start_link == -1:
			return None, 0
		start_quote = page.find('"', start_link)
		end_quote = page.find('"', start_quote + 1)
		getVideoID = page[start_quote + 1: end_quote].replace(self.watch_url, '')
		return getVideoID, end_quote


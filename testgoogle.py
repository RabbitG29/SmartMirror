#-*- coding: utf-8 -*-
import requests
import os
import speech_recognition as sr
from gtts import gTTS

def start():
	sample_rate = 48000
	chunk_size = 2048
	while(1):
		print('??')
		r = sr.Recognizer()
		r.energy_threshold = 4000
		r.non_speaking_duration = 0.2
		r.pause_threshold = 0.2
		with sr.Microphone(device_index=2, sample_rate = sample_rate, chunk_size = chunk_size) as source:
			print("talk")
			audio = r.listen(source)
		try:
			voice = r.recognize_google(audio,language='ko-KR')
			print(voice)
		except sr.UnknownValueError:
			continue
		except sr.RequestError as e:
			print(e)
		if((voice.find( u"나비")!=-1)):
			#os.system("source ../env/bin/activate")
			os.system("/home/pi/env/bin/googlesamples-assistant-pushtotalk --lang ko-KR --project-id raspi-assistant-a996b --device-model-id raspi-assistant-a996b-raspi-assistant-test-8xulbt")

if __name__=='__main__':
	start()

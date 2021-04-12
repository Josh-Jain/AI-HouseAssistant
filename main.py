import sys
import os

#import pyaudio
import yaml
import speech_recognition as sr

from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from brain import brain 
from greymatter.sensecells.tts import tts
from greymatter import play_music

profile = open('profile.yaml')
profile_data = yaml.safe_load(profile)
profile.close()

name = profile_data['Name']
country_name = profile_data['Country_Name']
music_path = profile_data['music_path']

#voice_file = os.getcwd() + '/uploads/' + sys.argv[1]
tts('Welcome '+ name +' systems are now ready to run. how can i help you?')

def main():
	r = sr.Recognizer()
	#with sr.WavFile(voice_file) as source:
	#	audio = r.record(source)
	with sr.Microphone() as source:
		print('say something!')
		audio = r.listen(source)

	try:
		speech_text = r.recognize_google(audio).lower().replace("'","") 
		print("Josh thinks you said '" + speech_text + "'")
	except sr.UnknownValueError:
    		print("Josh could not understand audio")
	except sr.RequestError as e:
    		print("could not request result from Google speech recgonition service; {0}".format(e))

	play_music.mp3gen(music_path)
	brain(name, speech_text, music_path)

main()

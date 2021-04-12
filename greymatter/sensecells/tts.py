import os 
import sys
import pyttsx3

def tts(message):

	if sys.platform == 'linux2' or sys.platform == 'linux':
		tts_engine = "espeak"
		return os.system(tts_engine + ' "' + message + '"')

import sys

from espeak import espeak
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from greymatter import general_conv
from greymatter import time, wiki, firefox, sleep, play_music, notes

def brain(name, speech_text, music_path):
	def check_message(check):
		words_of_message = speech_text.split()
		if set(check).issubset(set(words_of_message)):
			return True
		else:
			return False

	if check_message(['who', 'are', 'you']):
		general_conv.who_are_you()

	elif check_message(['hey', 'josh', 'who', 'am', 'i']):
		general_conv.who_am_i(name)

	elif check_message(['hey', 'josh', 'door', 'open']):
		general_conv.Door_open()
	elif check_message(['hey', 'josh', 'check']):
		general.conv.unknown()

	elif check_message(['hey', 'josh', 'time']):
		time.what_is_time()

	elif check_message(['hey', 'josh', 'define']):		
		wiki.wiki(speech_text)

	elif check_message(['hey', 'josh', 'open', 'firefox']):
		firefox.open_fox()

	elif check_message(['hey', 'josh', 'sleep']):
		sleep.go_to_sleep()

	elif check_message(['hey', 'josh', 'play']):
		play_music.play_random(music_path)

	elif check_message([ 'note']):
		notes.note_something(speech_text)

	elif check_message([ 'all', 'notes']):
		notes.show_all_notes()
	else:
		general_conv.undefined()

import sys
from os import path
sys.path.append(path.dirname(path.abspath(__file__)))
from sensecells.tts import tts

def who_are_you():
	message = 'I am Josh, your very own personal assistant.'
	tts(message)

def who_am_i(name):
	tts('your name is ' + name + ', you are my Boss')

def Door_open():
	tts('Doors opening')

def unknown():
	tts('there is an unknown person at the door, please come and verify')

def undefined():
	tts('I dont know what that means')

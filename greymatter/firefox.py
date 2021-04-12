from selenium import webdriver

from sensecells.tts import tts

def open_fox():
	tts('opening firefox')
	webdriver.Firefox()

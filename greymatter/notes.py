import sqlite3
from datetime import datetime

from sensecells.tts import tts

def note_something(speech_text):
	conn = sqlite3.connect('memory.db')
	words_of_message = speech_text.split()
	words_of_message.remove('note')
	cleaned_message = ' '.join(words_of_message)

	conn.execute("INSERT INTO notes (notes, notes_date) VALUES (?, ?)", (cleaned_message,datetime.strftime(datetime.now(), '%d-%m-%y')))
	conn.commit()
	conn.close()

	tts('Your notes has been saved.')

def show_all_notes():
	conn = sqlite3.connect('memory.db')
	tts('your notes are as follows:')

	cursor = conn.execute("SELECT notes FROM notes")
	for row in cursor:
		tts(row[0])

	conn.close()

import sqlite3

def get_connection():
	com = sqlite3.connect('articles.db')
	com.row_factory = sqlite3.Row # This enables column access by name
	return com
    
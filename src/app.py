from modules.Character import Character
from modules.database_manager import *
from modules.SQL_Character import SQL_Character
import sqlite3
connection = sqlite3.connect('src/python_quest.db')
cursor = connection.cursor()

character_data = get_characters(cursor, 1)
sql_erdrick = SQL_Character(character_data)
erdrick = Character(sql_erdrick)
erdrick.print_self()
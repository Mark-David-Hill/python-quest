from modules.Character import Character
from modules.database_manager import *
from modules.SQL_Character import SQL_Character
import sqlite3
connection = sqlite3.connect('src/python_quest.db')
cursor = connection.cursor()

character_data = get_characters(cursor)
sql_characters = [SQL_Character(character_data[0]), SQL_Character(character_data[1])]
# sql_erdrick = SQL_Character(character_data)
# erdrick = Character(sql_erdrick)
# erdrick.print_self()
characters = [Character(sql_characters[0]), Character(sql_characters[1])]
characters[0].print_self()
print('\n')
characters[1].print_self()

character_data_mark = get_characters(cursor, 'jk')
print(character_data_mark)
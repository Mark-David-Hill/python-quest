from modules.Character import Character
from modules.database_manager import *
from modules.SQL_Character import SQL_Character
from modules.get_date_time_str import get_date_time_str
import sqlite3
connection = sqlite3.connect('src/python_quest.db')
cursor = connection.cursor()

# character_data = get_characters(cursor)
# sql_characters = [SQL_Character(character_data[0]), SQL_Character(character_data[1])]
# # sql_erdrick = SQL_Character(character_data)
# # erdrick = Character(sql_erdrick)
# # erdrick.print_self()
# characters = [Character(sql_characters[0]), Character(sql_characters[1])]
# characters[0].print_self()
# print('\n')
# characters[1].print_self()

# character_data_mark = get_characters(cursor, 1)
# print(character_data_mark)


# def test_get_characters_by_id(cursor):
# character_data = get_characters(cursor, 2)
# print(character_data)
import random

# name = str(random.randint(0, 100000))
# level = str(random.randint(0, 30))
# exp = str(random.randint(0, 10000))
# hp = str(random.randint(0, 100000))
# mp = str(random.randint(0, 100000))
# weapon_id = str(random.randint(0, 100000))
# armor_id = str(random.randint(0, 100000))
# shield_id = str(random.randint(0, 100000))
# accessory_id = str(random.randint(0, 100000))
# inventory = str(random.randint(0, 100000))
# date_saved = get_date_time_str()
# cursor = connection.cursor()
# add_character(connection, name, level, exp, hp, mp, weapon_id, armor_id, shield_id, accessory_id, inventory, date_saved)
# all_characters = get_characters(cursor)
# test_character = all_characters[-1]
# print(all_characters)
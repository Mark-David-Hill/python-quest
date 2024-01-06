# from modules.Character import Character
# from modules.Hero import Hero
# from modules.Enemy import Enemy
# from modules.character_classes import *
# from modules.Hero import Hero\
import random
from modules.characters import *
from modules.database_manager import *
from modules.get_date_time_str import get_date_time_str
from modules.battle_manager import Battle_Manager
import sqlite3
import ansi_lib as al
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
# import random

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

# sql_data = get_characters(cursor, 1)
# sql_mark = SQL_Character(sql_data)
# # sql_mark.print_self()
# Mark = Hero(sql_mark)

# Mark.print_self()

battle_screen_layout = """
 _____________________    ___________________________________________________________
|                     |  |                                                           |
|                     |  |                                                           |
 _____________________   |                                                           |
 _____________________   |                                                           |
|                     |  |                                                           |
|    HP:              |  |                                                           |
|    MP:              |  |                                                           |
|    Level:           |  |                                                           |
 _____________________   |                                                           |
                         |                                                           |
 _____________________   |                                                           |
|                     |  |                                                           |
|   1. Attack         |  |                                                           |
|   2. Spells         |  |                                                           |
|   3. Flee           |  |                                                           |
|   4. Items          |  |                                                           |
|                     |  |                                                           |
 _____________________    ___________________________________________________________
 ____________________________________________________________________________________
|                                                                                    |
|                                                                                    |
|                                                                                    |
|                                                                                    |
|                                                                                    |
 ____________________________________________________________________________________
"""

slime_art = """
______________█_____________
______________█_____________
_____________███____________
__________███▒▒▒███_________
_______███▒▒▒▒▒▒▒▒▒███______
___████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████__
██▒▒▒▒▒▒▒▒██▒▒▒▒██▒▒▒▒▒▒▒▒██
██▒▒▒▒▒▒▒▒██▒▒▒▒██▒▒▒▒▒▒▒▒██
██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
██▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒██
██▓▓▒▒▒▒▒██████████▒▒▒▒▒▓▓██
__██▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓██__
____████████████████████____
"""

slime_art_list = [
'______________█_____________',
'______________█_____________',
'_____________███____________',
'__________███▒▒▒███_________',
'_______███▒▒▒▒▒▒▒▒▒███______',
'___████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████__',
'██▒▒▒▒▒▒▒▒██▒▒▒▒██▒▒▒▒▒▒▒▒██',
'██▒▒▒▒▒▒▒▒██▒▒▒▒██▒▒▒▒▒▒▒▒██',
'██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██',
'██▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒██',
'██▓▓▒▒▒▒▒██████████▒▒▒▒▒▓▓██',
'__██▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓██__',
'____████████████████████____'
]

# al.set_font(al.fg.blue, al.bg.black, al.text.bold)
al.clear()
al.set_font(al.fg.white, al.bg.black)

# print(battle_screen_layout)

sql_data = get_enemies(cursor, 1)
sql_slime = SQL_Enemy(sql_data)
# sql_slime.print_self()
slime = Enemy(sql_slime)
# slime.print_self()

sql_hero_data = get_characters(cursor, 1)
sql_hero = SQL_Character(sql_hero_data)
hero = Hero(sql_hero)
# hero.print_self()

bm = Battle_Manager(hero, slime, random, al)

bm.display_battle_menu()

# print('\n\n')

# for i in range(200):
# bm.attack_enemy()
# bm.attack_hero()

# print(random.random())

# al.move_cursor(24, 'u')
# # al.move_cursor(25, 'r')

# al.set_font(al.fg.blue, al.bg.black)
# for line in slime_art_list:
#   al.set_col(41)
#   al.writeln(line)
#   al.next_line()

# for i in range(10):
#   al.next_line()
# # print(slime_art)
  
# al.set_font(al.fg.white, al.bg.black)
  
# input('Please type the number corresponding to your desired action: ')
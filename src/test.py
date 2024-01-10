import random
from modules.characters import *
from modules.database_manager import *
from modules.get_date_time_str import get_date_time_str
from modules.battle_manager import Battle_Manager
import sqlite3
import ansi_lib as al
from modules.ansi_album import Ansi_Album
connection = sqlite3.connect('src/python_quest.db')
cursor = connection.cursor()

album = Ansi_Album()

sql_data = get_enemies(cursor, 1)
sql_slime = SQL_Enemy(sql_data)
slime = Enemy(sql_slime)

sql_hero_data = get_characters(cursor, 2)
sql_hero = SQL_Character(sql_hero_data)
hero = Hero(sql_hero)

bm = Battle_Manager(hero, slime, random, al, album)

bm.display_battle_menu()
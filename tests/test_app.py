# To test: PYTHONPATH=src python3 -m pytest
from modules.characters import Character
import pytest
import sqlite3
from src.modules.SQL_Character import SQL_Character
from modules.characters import Character
from src.modules.database_manager import *
from src.modules.SQL_Character import SQL_Character
from src.modules.get_date_time_str import get_date_time_str
import random

@pytest.fixture
def connection(tmpdir):
  'Provides a connection for the test Database'
  connection = sqlite3.connect("tests/python_quest.db")
  yield connection
  connection.close()

@pytest.fixture
def cursor(tmpdir):
  'Provides a cursor for the test Database'
  connection = sqlite3.connect("tests/python_quest.db")
  cursor = connection.cursor()
  yield connection
  connection.close()

def test_get_characters_by_id(cursor):
  character_data = get_characters(cursor, 2)
  assert character_data[1] == 'Mark'

def test_get_all_characters(cursor):
  character_data = get_characters(cursor)
  assert character_data[0][1] == 'Erdrick' and character_data[1][1] == 'Mark'

def test_get_character_by_wrong_id_returns_none(cursor):
  character_data = get_characters(cursor, 0)
  assert character_data is None

def test_get_character_by_string_returns_none(cursor):
  character_data = get_characters(cursor, 'monkey')
  assert character_data is None

def test_create_sql_character_works():
  sql_data = (1, 'Erdrick', 20, 0, None, None, 1, 1, 1, 1, None, '2023/12/20 07:13:23')
  sql_erdrick = SQL_Character(sql_data)
  assert sql_erdrick.character_id == 1 and sql_erdrick.name == 'Erdrick' and sql_erdrick.level == 20 and sql_erdrick.exp == 0 and sql_erdrick.weapon_id == 1 and sql_erdrick.armor_id == 1 and sql_erdrick.shield_id == 1 and sql_erdrick.accessory_id == 1 and sql_erdrick.date_saved == '2023/12/20 07:13:23'

def test_create_sql_character_from_database_works(cursor):
  sql_data = get_characters(cursor, 2)
  sql_mark = SQL_Character(sql_data)
  assert sql_mark.character_id == 2 and sql_mark.name == 'Mark' and sql_mark.level == 5 and sql_mark.exp == 0 and sql_mark.weapon_id == 1 and sql_mark.armor_id == 1 and sql_mark.shield_id == 1 and sql_mark.accessory_id == 1

def test_create_character():
  sql_data = (1, 'Erdrick', 20, 15, 35, 25, 8, 9, 10, 11, '6, 2, 5, 8', '2023/12/20 07:13:23')
  sql_erdrick = SQL_Character(sql_data)
  erdrick = Character(sql_erdrick)
  assert erdrick.id == 1 and erdrick.name == 'Erdrick' and erdrick.level == 20 and erdrick.exp == 15 and erdrick.hp == 35 and erdrick.mp == 25 and erdrick.weapon_id == 8 and erdrick.armor_id == 9 and erdrick.shield_id == 10 and erdrick.accessory_id == 11 and erdrick.inventory_str == '6, 2, 5, 8' and erdrick.date_saved == '2023/12/20 07:13:23'

def test_create_character_from_database_works(cursor):
  sql_data = get_characters(cursor, 2)
  sql_mark = SQL_Character(sql_data)
  mark = Character(sql_mark)
  assert mark.id == 2 and mark.name == 'Mark'

def test_get_datetime_str_returns_str():
  datetime_str = get_date_time_str()
  assert isinstance(datetime_str, str)

def test_add_character_works(connection):
  name = str(random.randint(0, 100000))
  level = str(random.randint(0, 30))
  exp = str(random.randint(0, 10000))
  hp = str(random.randint(0, 100000))
  mp = str(random.randint(0, 100000))
  weapon_id = str(random.randint(0, 100000))
  armor_id = str(random.randint(0, 100000))
  shield_id = str(random.randint(0, 100000))
  accessory_id = str(random.randint(0, 100000))
  inventory = str(random.randint(0, 100000))
  date_saved = get_date_time_str()
  cursor = connection.cursor()
  add_character(connection, name, level, exp, hp, mp, weapon_id, armor_id, shield_id, accessory_id, inventory, date_saved)
  all_characters = get_characters(cursor)
  test_character = all_characters[-1]
  assert test_character[1] == name

# def test_get_growth_type_returns_expected_1():
#   character = Character()
#   growth_sum = character.get_growth_sum('Erdrick')
#   growth_type = character.get_growth_type(growth_sum)
#   assert growth_sum == 43 and growth_type == 3

# def test_get_growth_type_returns_expected_2():
#   character = Character()
#   growth_sum = character.get_growth_sum('Mark')
#   growth_type = character.get_growth_type(growth_sum)
#   assert growth_sum == 25 and growth_type == 1

# def test_get_growth_type_returns_expected_3():
#   character = Character()
#   growth_sum = character.get_growth_sum('A')
#   growth_type = character.get_growth_type(growth_sum)
#   assert growth_sum == 4 and growth_type == 0

# def test_get_growth_type_returns_expected_4():
#   character = Character()
#   growth_sum = character.get_growth_sum('★&^#@$m')
#   growth_type = character.get_growth_type(growth_sum)
#   assert growth_sum == 6 and growth_type == 2

# def test_get_growth_type_returns_expected_5():
#   character = Character()
#   growth_sum = character.get_growth_sum('★&^#@$')
#   growth_type = character.get_growth_type(growth_sum)
#   assert growth_sum == 0 and growth_type == 0
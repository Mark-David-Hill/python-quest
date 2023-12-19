# To test: PYTHONPATH=src python3 -m pytest
from src.modules.Character import Character
import pytest
import sqlite3
from src.modules.Character import Character
from src.modules.database_manager import *
from src.modules.SQL_Character import SQL_Character

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
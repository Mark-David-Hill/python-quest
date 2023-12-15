# To test: PYTHONPATH=src python3 -m pytest
from src.modules.Character import Character

def test_get_growth_type_returns_expected_1():
  character = Character()
  growth_type = character.get_growth_type('Erdrick')
  assert growth_type == 3

def test_get_growth_type_returns_expected_2():
  character = Character()
  growth_type = character.get_growth_type('Mark')
  assert growth_type == 1

def test_get_growth_type_returns_expected_3():
  character = Character()
  growth_type = character.get_growth_type('A')
  assert growth_type == 0

def test_get_growth_type_returns_expected_4():
  character = Character()
  growth_type = character.get_growth_type('★&^#@$m')
  assert growth_type == 2

def test_get_growth_type_returns_expected_5():
  character = Character()
  growth_type = character.get_growth_type('★&^#@$')
  assert growth_type == 0
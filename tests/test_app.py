# To test: PYTHONPATH=src python3 -m pytest
from src.modules.Character import Character

def test_get_growth_type_returns_expected_1():
  character = Character()
  growth_sum = character.get_growth_sum('Erdrick')
  growth_type = character.get_growth_type(growth_sum)
  assert growth_sum == 43 and growth_type == 3

def test_get_growth_type_returns_expected_2():
  character = Character()
  growth_sum = character.get_growth_sum('Mark')
  growth_type = character.get_growth_type(growth_sum)
  assert growth_sum == 25 and growth_type == 1

def test_get_growth_type_returns_expected_3():
  character = Character()
  growth_sum = character.get_growth_sum('A')
  growth_type = character.get_growth_type(growth_sum)
  assert growth_sum == 4 and growth_type == 0

def test_get_growth_type_returns_expected_4():
  character = Character()
  growth_sum = character.get_growth_sum('★&^#@$m')
  growth_type = character.get_growth_type(growth_sum)
  assert growth_sum == 6 and growth_type == 2

def test_get_growth_type_returns_expected_5():
  character = Character()
  growth_sum = character.get_growth_sum('★&^#@$')
  growth_type = character.get_growth_type(growth_sum)
  assert growth_sum == 0 and growth_type == 0
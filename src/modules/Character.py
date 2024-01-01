# implement active variable into tests/other classes
# Implement Level Up Check/Level Up
# Implement Saving Character to DB

class Character:
  def __init__(self):
    self.id = 0
    self.name = 0
    self.hp = 0
    self.mp = 0
    self.str = 0
    self.agi = 0
    self.max_hp = 0
    self.max_mp = 0

  def print_self(self):
    print(f'ID: {self.id}')
    print(f'Name: {self.name}')
    print(f'HP: {self.hp}')
    print(f'MP: {self.mp}')
    print(f'STR: {self.str}')
    print(f'AGI: {self.agi}')
    print(f'Max HP: {self.max_hp}')
    print(f'Max MP: {self.max_mp}')

  def check_for_ko(self):
    if self.hp <= 0:
      return True
    else:
      return False
from Character import Character

class Enemy(Character):
  def __init__(self, sql_enemy):
    self.id = sql_enemy.sql_enemy.character_id
    self.name = sql_enemy.name
    self.max_hp = sql_enemy.max_hp
    self.max_mp = sql_enemy.max_mp
    self.str = sql_enemy.str
    self.agi = sql_enemy.agi
    self.max_hp = sql_enemy.max_hp
    self.max_mp = sql_enemy.max_hp

  def print_self(self):
    print(f'ID: {self.id}')
    print(f'Name: {self.name}')
    print(f'STR: {self.str}')
    print(f'AGI: {self.agi}')
    print(f'Max HP: {self.max_hp}')
    print(f'Max MP: {self.max_mp}')
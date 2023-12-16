class Character:
  def __init__(self, sql_character):
    self.character.id = sql_character.character_id
    self.name = sql_character.name
    self.level = sql_character.level
    self.exp = sql_character.exp
    self.hp = sql_character.hp
    self.mp = sql_character.mp
    self.weapon_id = sql_character.weapon_id
    self.armor_id = sql_character.weapon_id
    self.shield_id = sql_character.shield_id
    self.accessory_id = sql_character.accessory_id
    self.inventory_str = sql_character.inventory

  def get_growth_sum(self, name):
    letter_values = [
      ["g", "w", "M", "'"], 
      ['h', 'x', 'N'],
      ['i', 'y', 'O'],
      ['j', 'z', 'P'],
      ['k', 'A', 'Q'],
      ['l', 'B', 'R'],
      ['m', 'C', 'S'],
      ['n', 'D', 'T'],
      ['o', 'E', 'U', ','],
      ['p', 'E', 'U'],
      ['a', 'q', 'G', 'W'],
      ['b', 'r', 'H', 'X', '?'],
      ['c', 's', 'I', 'Y', '!'],
      ['d', 't', 'J', 'Z'],
      ['e', 'e', 'K', ')'],
      ['f', 'v', 'L', '(']
    ]
    growth_sum = 0
    letter_count = 0
    for letter in name:
      if letter_count < 4:
        for i in range(len(letter_values)):
          if letter in letter_values[i]:
            growth_sum += i
            letter_count += 1
            break
    return growth_sum

  def get_growth_type(self, growth_sum):
    growth_type = growth_sum % 4
    return growth_type

  def get_base_stats(self):
    strength_stats_by_level = [0, 4, 5, 7, 7, 12, 16, 18, 22, 30, 35, 40, 48, 52, 60, 68, 72, 72, 85, 87, 92, 95, 97, 99, 103, 113, 117, 125, 130, 135, 140]
    agility_stats_by_level = [0, 4, 4, 6, 8, 10, 10, 17, 20, 22, 31, 35, 40, 48, 55, 64, 70, 78, 84, 86, 88, 90, 90, 94, 98, 100, 105, 107, 115, 120, 130]
    max_hp_by_level = [0, 15, 22, 24, 31, 35, 38, 40, 46, 50, 54, 62, 63, 70, 78, 86, 92, 100, 115, 130, 138, 149, 158, 165, 170, 174, 180, 189, 195, 200, 210]
    max_mp_by_level = [0, 0, 0, 5, 16, 20, 24, 26, 29, 36, 40, 50, 58, 64, 70, 72, 95, 100, 108, 115, 128, 135, 146, 153, 161, 161, 168, 175, 180, 190, 200]


# character = Character()
# growth_type = character.get_growth_type('Erdrick')
# print(growth_type)
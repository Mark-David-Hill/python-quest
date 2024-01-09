# implement active variable into tests/other classes
# Implement Saving Character to DB
# https://gamefaqs.gamespot.com/nes/563408-dragon-warrior/faqs/69121

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
    





class Hero(Character):
  def __init__(self, sql_character):
    self.id = sql_character.character_id
    self.name = sql_character.name
    self.level = sql_character.level
    self.exp = sql_character.exp
    self.hp = sql_character.hp
    self.mp = sql_character.mp
    self.weapon_id = sql_character.weapon_id
    self.armor_id = sql_character.armor_id
    self.shield_id = sql_character.shield_id
    self.accessory_id = sql_character.accessory_id
    self.inventory_str = sql_character.inventory
    self.date_saved = sql_character.date_saved
    self.growth_sum = self.get_growth_sum(self.name)
    self.growth_type = self.get_growth_type(self.growth_sum)
    self.growth_quotient = self.growth_sum // 4
    self.stat_modifier = self.growth_quotient % 4
    self.str = self.get_strength()
    self.agi = self.get_agility()
    self.max_hp = self.get_max_hp()
    self.max_mp = self.get_max_mp()
    if self.hp is None:
      self.hp = self.max_hp
    if self.mp is None:
      self.mp = self.max_mp

  def print_self(self):
    print(f'ID: {self.id}')
    print(f'Name: {self.name}')
    print(f'Level: {self.level}')
    print(f'EXP: {self.exp}')
    print(f'HP: {self.hp}')
    print(f'MP: {self.mp}')
    print(f'Weapon ID: {self.weapon_id}')
    print(f'Armor ID: {self.armor_id}')
    print(f'Shield ID: {self.shield_id}')
    print(f'Accessory ID: {self.accessory_id}')
    print(f'Inventory STR: {self.inventory_str}')
    print(f'Date Saved: {self.date_saved}')
    print(f'Growth Sum: {self.growth_sum}')
    print(f'Growth Type: {self.growth_type}')
    print(f'STR: {self.str}')
    print(f'AGI: {self.agi}')
    print(f'Max HP: {self.max_hp}')
    print(f'Max MP: {self.max_mp}')
    print(f'Stat Modifier: {self.stat_modifier}')

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

  def get_strength(self):
    strength_stats_by_level = [0, 4, 5, 7, 7, 12, 16, 18, 22, 30, 35, 40, 48, 52, 60, 68, 72, 72, 85, 87, 92, 95, 97, 99, 103, 113, 117, 125, 130, 135, 140]
    if self.growth_type == 0 or self.growth_type == 2:
      modified_str = int((strength_stats_by_level[self.level] * (9/10)) + self.stat_modifier)
      return modified_str
    else:
      base_str = strength_stats_by_level[self.level]
      return base_str
  
  def get_agility(self):
    agility_stats_by_level = [0, 4, 4, 6, 8, 10, 10, 17, 20, 22, 31, 35, 40, 48, 55, 64, 70, 78, 84, 86, 88, 90, 90, 94, 98, 100, 105, 107, 115, 120, 130]
    if self.growth_type == 0 or self.growth_type == 1:
      modified_agi = int((agility_stats_by_level[self.level] * (9/10)) + self.stat_modifier)
      return modified_agi
    else:
      base_agi = agility_stats_by_level[self.level]
      return base_agi

  def get_max_hp(self):
    max_hp_by_level = [0, 15, 22, 24, 31, 35, 38, 40, 46, 50, 54, 62, 63, 70, 78, 86, 92, 100, 115, 130, 138, 149, 158, 165, 170, 174, 180, 189, 195, 200, 210]
    if self.growth_type == 2 or self.growth_type == 3:
      modified_max_hp = int((max_hp_by_level[self.level] * (9/10)) + self.stat_modifier)
      return modified_max_hp
    else:
      base_max_hp = max_hp_by_level[self.level]
      return base_max_hp
  
  def get_max_mp(self):
    max_mp_by_level = [0, 0, 0, 5, 16, 20, 24, 26, 29, 36, 40, 50, 58, 64, 70, 72, 95, 100, 108, 115, 128, 135, 146, 153, 161, 161, 168, 175, 180, 190, 200]
    if self.growth_type == 1 or self.growth_type == 3:
      modified_max_mp = int((max_mp_by_level[self.level] * (9/10)) + self.stat_modifier)
      return modified_max_mp
    else:
      base_max_mp = max_mp_by_level[self.level]
      return base_max_mp
    
  def check_for_level_up(self):
    pass

  def level_up(self):
    pass
    




class Enemy(Character):
  def __init__(self, sql_enemy):
    self.id = sql_enemy.enemy_id
    self.name = sql_enemy.name
    self.max_hp = sql_enemy.max_hp
    self.max_mp = sql_enemy.max_mp
    self.str = sql_enemy.str
    self.agi = sql_enemy.agi
    self.max_hp = sql_enemy.max_hp
    self.max_mp = sql_enemy.max_hp
    self.hp = self.max_hp
    self.evasion = sql_enemy.evasion

  def print_self(self):
    print(f'ID: {self.id}')
    print(f'Name: {self.name}')
    print(f'STR: {self.str}')
    print(f'AGI: {self.agi}')
    print(f'Max HP: {self.max_hp}')
    print(f'Max MP: {self.max_mp}')









class SQL_Character:
  def __init__(self, sql_data):
    self.sql_data = sql_data
    self.character_id = sql_data[0]
    self.name = sql_data[1]
    self.level = sql_data[2]
    self.exp = sql_data[3]
    self.hp = sql_data[4]
    self.mp = sql_data[5]
    self.weapon_id = sql_data[6]
    self.armor_id = sql_data[7]
    self.shield_id = sql_data[8]
    self.accessory_id = sql_data[9]
    self.inventory = sql_data[10]
    self.date_saved = sql_data[11]

  def print_self(self):
    print(f'Character ID: {self.character_id}')
    print(f'Name: {self.name}')
    print(f'Level: {self.level}')
    print(f'EXP: {self.exp}')
    print(f'HP: {self.hp}')
    print(f'MP: {self.mp}')
    print(f'Weapon ID: {self.weapon_id}')
    print(f'Armor ID: {self.armor_id}')
    print(f'Shield ID: {self.shield_id}')
    print(f'Accessory ID: {self.accessory_id}')
    print(f'Inventory: {self.inventory}')
    print(f'Date Saved: {self.date_saved}')


class SQL_Enemy:
  def __init__(self, sql_data):
    self.sql_data = sql_data
    self.enemy_id = sql_data[0]
    self.name = sql_data[1]
    self.dw_name = sql_data[2]
    self.str = sql_data[3]
    self.agi = sql_data[4]
    self.max_hp = sql_data[5]
    self.max_mp = sql_data[6]
    self.exp = sql_data[7]
    self.gold = sql_data[8]
    self.spell_1_id = sql_data[9]
    self.spell_1_chance = sql_data[10]
    self.spell_2_id = sql_data[11]
    self.spell_2_chance = sql_data[12]
    self.spell_3_id = sql_data[13]
    self.spell_3_chance = sql_data[14]
    self.sleep_resist = sql_data[15]
    self.stopspell_resist = sql_data[16]
    self.hurt_resist = sql_data[17]
    self.evasion = sql_data[18]

  def print_self(self):
    print(f'Enemy ID: {self.enemy_id}')
    print(f'Name: {self.name}')
    print(f'DW Name: {self.dw_name}')
    print(f'STR: {self.str}')
    print(f'AGI: {self.agi}')
    print(f'Max HP: {self.max_hp}')
    print(f'Max MP: {self.max_mp}')
    print(f'EXP: {self.exp}')
    print(f'Gold: {self.gold}')
    print(f'Sleep Resist: {self.sleep_resist}')
    print(f'Stopspell Resist: {self.stopspell_resist}')
    print(f'Hurt Resist: {self.hurt_resist}')
    print(f'Evasion: {self.evasion}')
    print(f'Spell 1 ID: {self.spell_1_id}')
    print(f'Spell 1 Chance: {self.spell_1_chance}')
    print(f'Spell 2 ID: {self.spell_2_id}')
    print(f'Spell 2 Chance: {self.spell_2_chance}')
    print(f'Spell 3 ID: {self.spell_3_id}')
    print(f'Spell 3 Chance: {self.spell_3_chance}')
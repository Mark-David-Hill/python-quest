class Battle_Manager:
  def __init__(self, hero, enemy, random, ansi_lib) -> None:
    self.hero = hero
    self.enemy = enemy
    self.random = random
    self.al = ansi_lib

  def battle_start(self):
    pass

  def check_for_enemy_ko(self):
    if(self.enemy.hp <= 0):
      print(f"{self.enemy.name} Was defeated!")
      return True
    else:
      return False
    
  def check_for_hero_ko(self):
    if(self.hero.hp <= 0):
      print(f"{self.hero.name} Was defeated.")
      return True
    else:
      return False
    
  def attack_hero(self):
      str = self.enemy.str
      print(f"The enemy's STR is {str}")

  # Chance to dodge, critical hit chance
  def attack_enemy(self):
    r = self.random
    evasion = self.enemy.evasion
    hit_attempt = r.random()
    print(f"Evasion: {evasion}. Hit Attempt: {hit_attempt}")
    if hit_attempt > evasion:
      hero_attack = self.hero.str
      enemy_agi = self.enemy.agi
      dmg = hero_attack - enemy_agi
      self.enemy.hp -= dmg
      print(f"{self.hero.name} Attacks the {self.enemy.name}. He deals {dmg} Damage!")
      self.check_for_enemy_ko()
    else:
      print(f"The Hero's attack missed!")

    
  
  def attempt_to_flee(self):
    pass

  

  def display_battle_menu(self):
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
    print(battle_screen_layout)

enemy_origin = [27, 26]
hp_origin = [13, 21]

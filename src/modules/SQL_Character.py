class SQL_Character:
  def __init__(self, sql_data):
    self.sql_data = sql_data
    self.character_id = sql_data[0]
    self.name = sql_data[1]
    self.name = sql_data[2]
    self.level = sql_data[3]
    self.exp = sql_data[4]
    self.hp = sql_data[5]
    self.mp = sql_data[6]
    self.weapon_id = sql_data[7]
    self.armor_id = sql_data[8]
    self.shield_id = sql_data[9]
    self.accessory_id = sql_data[10]
    self.inventory = sql_data[11]
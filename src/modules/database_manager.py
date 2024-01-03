import datetime

def get_characters(cursor, character_id = -1):
  try:
    sql_select = None
    if character_id == -1:
      sql_select = '''
        SELECT character_id, name, level, exp, hp, mp, weapon_id, armor_id, shield_id, accessory_id, inventory, date_saved
        FROM Characters WHERE active = 1
      '''
      rows = cursor.execute(sql_select).fetchall()
      return rows
      
    else:
      sql_select = '''
        SELECT character_id, name, level, exp, hp, mp, weapon_id, armor_id, shield_id, accessory_id, inventory, date_saved
        FROM Characters WHERE character_id = ?
      '''
      rows = cursor.execute(sql_select, (character_id,)).fetchone()
      return rows
    
  except Exception as e:
    print(f'\n- ERROR: {e}. Could not get Character data.')

def add_character(connection, name, level, exp, hp, mp, weapon_id, armor_id, shield_id, accessory_id, inventory, date_saved):
  insert_sql = 'INSERT INTO Characters (name, level, exp, hp, mp, weapon_id, armor_id, shield_id, accessory_id, inventory, date_saved) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
  try:
    cursor = connection.cursor()
    cursor.execute(insert_sql, (name, level, exp, hp, mp, weapon_id, armor_id, shield_id, accessory_id, inventory, date_saved))
    connection.commit()
    print(f'\nSUCCESS: Character "{name}" Successfully created!')
  except Exception as e:
    print(f'\n- ERROR: {e}. Character was not created.')


def get_enemies(cursor, enemy_id = -1):
  try:
    sql_select = None
    if enemy_id == -1:
      sql_select = '''
        SELECT enemy_id, name, dw_name, str, agi, max_hp, max_mp, exp, gold, spell_1_id, spell_1_chance, spell_2_id, spell_2_chance, spell_3_id, spell_3_chance, sleep_resist, stopspell_resist, hurt_resist, evasion
        FROM Enemies WHERE active = 1
      '''
      rows = cursor.execute(sql_select).fetchall()
      return rows
      
    else:
      sql_select = '''
        SELECT enemy_id, name, dw_name, str, agi, max_hp, max_mp, exp, gold, spell_1_id, spell_1_chance, spell_2_id, spell_2_chance, spell_3_id, spell_3_chance, sleep_resist, stopspell_resist, hurt_resist, evasion
        FROM Enemies WHERE enemy_id = ?
      '''
      rows = cursor.execute(sql_select, (enemy_id,)).fetchone()
      return rows
    
  except Exception as e:
    print(f'\n- ERROR: {e}. Could not get Character data.')
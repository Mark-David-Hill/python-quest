import datetime

def get_characters(cursor, character_id = -1):
  try:
    sql_select = None
    if character_id == -1:
      sql_select = '''
        SELECT character_id, name, level, exp, hp, mp, weapon_id, armor_id, shield_id, accessory_id, inventory, date_saved
        FROM Characters
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
def get_characters(cursor, character_id = -1):
  try:
    sql_select = None
    if character_id == -1:
      sql_select = '''
        SELECT character_id, name, level, exp, hp, mp, weapon_id, armor_id, shield_id, accessory_id, inventory
        FROM Characters
      '''
      rows = cursor.execute(sql_select).fetchall()
      return rows
      
    else:
      sql_select = '''
        SELECT character_id, name, level, exp, hp, mp, weapon_id, armor_id, shield_id, accessory_id, inventory
        FROM Characters WHERE character_id = ?
      '''
      rows = cursor.execute(sql_select, (character_id,)).fetchone()
      return rows
    
  except Exception as e:
    print(f'\n- ERROR: {e}. Could not get Character data.')
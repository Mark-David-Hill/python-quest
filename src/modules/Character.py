class Character:
  def __init__(self):
    pass

  def get_growth_type(self, name):
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
    total_value = 0
    letter_count = 0
    for letter in name:
      if letter_count < 4:
        for i in range(len(letter_values)):
          if letter in letter_values[i]:
            total_value += i
            letter_count += 1
            break
    growth_type = total_value % 4
    return growth_type

  def get_base_stats(self, name):
    pass


# character = Character()
# growth_type = character.get_growth_type('Erdrick')
# print(growth_type)
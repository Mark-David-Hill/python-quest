class Battle_Manager:
    def __init__(self, hero, enemy, random, ansi_lib, album) -> None:
        self.hero = hero
        self.enemy = enemy
        self.random = random
        self.al = ansi_lib
        self.album = album
        self.menu_height = 26
        self.hero_name_origin = [5, 25]
        self.hero_hp_origin = [13, 21]
        self.mp_origin = [13, 20]
        self.level_origin = [13, 19]
        self.enemy_origin = [27, 26]

    def battle_start(self):
        pass

    def check_for_enemy_ko(self):
        if (self.enemy.hp <= 0):
            print(f"{self.enemy.name} Was defeated!")
            return True
        else:
            return False

    def check_for_hero_ko(self):
        if (self.hero.hp <= 0):
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

    def get_remaining_lines(self, vertical_position):
        lines_difference = self.menu_height - vertical_position
        remaining_lines = self.menu_height - lines_difference
        return remaining_lines

    def display(self, text_to_display, origin, offset=[0, 0]):
        x_origin = origin[0] + offset[0]
        y_origin = origin[1] + offset[1]
        self.al.set_col(x_origin)
        self.al.move_cursor(y_origin, 'u')
        self.al.writeln(text_to_display)
        remaining_lines = self.get_remaining_lines(origin[1])
        for _ in range(remaining_lines):
            self.al.next_line()

    def display_list(self, list_to_display, origin, offset=[0, 0]):
        x_origin = origin[0] + offset[0]
        y_origin = origin[1] + offset[1]
        self.al.set_col(x_origin)
        self.al.move_cursor(y_origin, 'u')

        for line in list_to_display:
            self.al.set_col(x_origin)
            self.al.writeln(line)
            self.al.next_line()

        remaining_lines = self.get_remaining_lines(origin[1])
        for _ in range(remaining_lines):
            self.al.next_line()

    def display_battle_menu(self):
        self.al.clear()
        print(self.album.battle_screen_layout)
        name = self.hero.name
        hp = self.hero.hp
        mp = self.hero.mp
        level = self.hero.level
        lengths = [len(str(hp)), len(str(mp)), len(str(level))]
        digits = [(3 - lengths[0]), (3 - lengths[1]), (3 - lengths[2])]
        self.display(self.hero.name, self.hero_name_origin, [0, 0])
        self.display(self.hero.hp, self.hero_hp_origin, [digits[0], 0])
        self.display(self.hero.mp, self.mp_origin, [digits[1], 0])
        self.display(self.hero.level, self.level_origin, [digits[2], 0])

        slime_list = self.album.slime_list
        self.display_list(slime_list, self.enemy_origin, [0, 0])

        # for _ in range(10):
        #   self.al.next_line()


def start_battle(self):
    self.display_battle_menu()

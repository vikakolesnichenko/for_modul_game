from settings import *
import random
from exceptions import EnemyDown
from exceptions import GameOver

class Enemy:
    def __init__(self):
        self.level = ENEMY_LEVEL
        self.lives = ENEMY_LEVEL


    @staticmethod
    def select_attack():
        number_attack = random.randrange(1, 4)
        return number_attack

    def decrease_lives(self):
        self.lives -= 1
        try:
            self.lives != 0
        except:
            EnemyDown


class Player:
    def __init__(self, name):
        self.name = name
        self.lives = PLAYER_LIVES
        self.score = SCORE
        self.allowed_attacks = ATTACKS

    @staticmethod
    def fight(attack, defense):
        if (attack == 1 and defense == 3) or (attack == 2 and defense == 1) or (attack == 3 and defense == 2):
            return -1
        if (attack == 1 and defense == 1) or (attack == 2 and defense == 2) or (attack == 3 and defense == 3):
            return 0
        if (attack == 1 and defense == 2) or (attack == 2 and defense == 3) or (attack == 3 and defense == 1):
            return 1

    def decrease_lives(self):
        self.lives -= 1
        if self.lives == 0:
            raise GameOver(name=self.name, score=self.score)


    def attack(self, enemy_obj):
        etalon_attack = 0
        while etalon_attack not in ATTACKS:
            try:
                etalon_attack = int(input("Select yuor attack: \n1 - Wizard 2 - Warrior 3 - Robber\n"))
                if etalon_attack not in ATTACKS:
                    raise ValueError
            except ValueError:
                print('Select correct attack, PLEASEEEEE!!!')


        enemy_obj.attack = enemy_obj.select_attack()
        battle = self.fight(etalon_attack, enemy_obj.select_attack())
        if battle == 0:
            print("It's a draw!\n")
        if battle == 1:
            print("You attacked successfully!\n")
            self.score += 1
            enemy_obj.decrease_lives()
        if battle == -1:
            print("You missed!\n")

    def defence(self, enemy_obj):
        etalon_defence = 0
        while etalon_defence not in ATTACKS:
            try:
                etalon_defence = int(input("Select yuor defence: \n1 - Wizard 2 - Warrior 3 - Robber\n"))
                if etalon_defence not in ATTACKS:
                    raise ValueError
            except ValueError:
                print('Select correct defence, PLEASEEEEE!!!')

        enemy_obj.attack = Enemy.select_attack()
        battle = self.fight(enemy_obj.select_attack(), etalon_defence)
        if battle == 0:
            print("It's a draw!\n")
        if battle == 1:
            print("Enemy attacked successfully!\n")
            self.decrease_lives()
        if battle == -1:
            print("Enemy missed!\n")



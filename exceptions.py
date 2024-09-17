from models import *
from game import *

class GameOver(Exception):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    @staticmethod
    def for_write_scores(name, score):
        print(f"{name}, your number of scores {score}")
        for_write_scores = open("scores.txt", 'a+')
        for_write_scores.write(f"{name}: points {score}\n")
        for_write_scores.close()


class EnemyDown(Exception):
    pass


class Score:
    pass

from models import *
import exceptions


def play():
    name = str(input("Please, enter your name: \n"))
    player = Player(name)
    enemy = Enemy()

    etalon = 'start'
    begin_of_game = input('Enter "start" to start the game: \n')
    while etalon != begin_of_game:
        begin_of_game = input('Enter "start" to start the game, PLEASEEEEEEE: \n')

    if begin_of_game == "start":
        print(f"{name}, welcome to the game")
        while True:
            try:
                player.attack(enemy)
                player.defence(enemy)
                if player.attack(enemy) == "You attacked successfully":
                    enemy.decrease_lives()
            except exceptions.EnemyDown:
                player.score += 5
                print(f"Your score: {player.score}")
                enemy.level += 1
                enemy.live = enemy.level
                print(f"Enemy status: {enemy.live}, {enemy.level}")
            except GameOver as err:
                err.for_write_scores(name=player.name, score=player.score)
                break


if __name__ == '__main__':

    try:
        play()
    except exceptions.GameOver: \
            print("It's all")
    finally:
        print("Good bye")

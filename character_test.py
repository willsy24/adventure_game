# Write your code here :-)
from character import Enemy
dave = Enemy("Dave", "A smelly zombie")
dave.describe()
dave.set_conversation("Braiiiinnnnss!!")
dave.set_weakness ("cheese")
game_over=False

def talk():
    print("What do you wish to say?")
    chat = input ("> ").lower()
    dave.talk()


def fight():
    print("What will you fight with?")
    fight_with = input("> ").lower
    dave.fight(fight_with)


while game_over is not True:
    print("What do you wish to do?")
    command = input("> ").lower()
    if command == "quit":
        print("Game Over\nPlease return again some day\n")
        game_over = True
    elif command == "talk":
        talk()
    elif command == "fight":
        fight()
        game_over= True


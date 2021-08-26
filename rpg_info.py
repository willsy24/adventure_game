class RPGInfo():
    author = "Anonymous"
    def __init__(self, game_title):
        self.title = game_title

    def welcome(self):
        print("Welcome to " + self.title)# Write your code here :-)

    @staticmethod
    def info():
        print("Made using the OOP RPG game creator (c) me")

    @staticmethod
    def commands():
        print ("north, south, east, west, up, down - move in a direction")
        print ("fight - fight a character")
        print ("give - give an object to a character")
        print ("hug - hug a character")
        print ("inventory - list items in your backpack")
        print ("look - describe the room")
        print ("read - read a book")
        print ("talk - have a conversation with a character")
        print ("take - take an object")





    @classmethod
    def credits(cls):
        print("Thank you for playing")
        print("Created by " + cls.author)


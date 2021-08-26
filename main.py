
from room import Room
from item import Item
from character import Enemy
from character import Friend
from rpg_info import RPGInfo


#backpack

backpack=[]

#functions

## asks which weapon will be used and if it is being carried.
## calls routine in Enemy class (inhabitant.fight) that will check if correct weapon is used.

def fight(inhabitant):
    print("What will you fight with?")
    fight_with = input("> ").lower
    if fight_with() in backpack:
        if inhabitant.fight(fight_with)==True:
            return True
        else:
            return False
    else:
        print ("You rummage through your backpack for your weapon. However you don't have one!")

## asks which gift wants to be given and checks whether it is owned.
## calls the inhabitant.give routine which checks to see if it  is the correct gift.
## contains the end game success code.

def give (inhabitant):
    print ("What do you want to give them?")
    gift_given = input("> ").lower
    if gift_given() in backpack:
        if inhabitant.give(gift_given) == True:
            backpack.remove(gift_given())
            print (Friend.happy)
        if Friend.happy == Friend.number_of_friends:
            print ("Congratulations, you have made the house happy. Well Done!")
            return True
    else:
        print ("You don't have one of those")

def hug(inhabitant):
    inhabitant.hug()

## asks which item wants to be taken and checks that it is in room.
## checkis if it is not a book.
## then puts item in backpack
## mostly code in to adjust to allow more than one item in room
## if this is done note, examine code will need to change.

def take(item_name):

    print ("What do you wish to take?")
    take_item = input ("> ").lower
    if take_item() == item_name:
        if item_name == "book":
            print ("A loud voice booms. 'HANDS OFF, REFERENCE ONLY!'")
        else:
            print ("You quickly place the ", item_name," in your backpack ")
            backpack.append (item_name)
            current_room.set_item(None)
    else:
        print ("That item is not here")

##contains talk command  routine. Asks what player wants to say.
## at present this has no extra function but could add further responses to specific prompts.

def talk(inhabitant):
    print("What do you wish to say?")
    chat = input ("> ").lower()
    inhabitant.talk()

#rooms
kitchen = Room("kitchen")
kitchen.set_description("A narrow room. The aroma of recently cooked food is in the air")

hall = Room("hall")
hall.set_description("A room that serves the purpose of linking the other rooms in the house. There seems to be a lot of gin here.")

living_room = Room ("living_room")
living_room.set_description("This room is full of comfy sofas, a TV and several games consoles.")

dining_room = Room ("dining hall")
dining_room.set_description ("This room is set with a dining table in the middle. Unusually, it is full of board games and sewing paraphrenalia")

utility_room = Room ("utility room")
utility_room.set_description ("This room contains a boiler, a washing machine and a fridge.")

landing = Room ("landing")
landing.set_description("This serves connects the upper rooms")

main_bedroom = Room ("Main Bedroom")
main_bedroom.set_description("A large bedroom with an equally large bed.")

teen_room = Room ("Teen(ish) Room")
teen_room.set_description ("This supposedly has a bed and supposedly has a floor. Neither can be seen due to the carpet of strewn clothes")

child_room = Room ("Child's Room.")
child_room.set_description("There seem to be many, many wild animals all over the bed here")

bathroom = Room ("Bathroom")
bathroom.set_description("A bath, a toilet, some toiletries. Some of this smells pleasant, some does not!")

garden = Room ("Garden")
garden.set_description("Some decking, some grass, some flowers.")

#mapping

hall.link_room(dining_room,"east")
hall.link_room(kitchen,"north")
hall.link_room(living_room,"west")
hall.link_room(landing,"up")

landing.link_room(bathroom, "north")
landing.link_room(main_bedroom,"east")
landing.link_room(teen_room,"west")
landing.link_room(child_room,"south")
landing.link_room(hall,"down")

dining_room.link_room(hall,"west")
kitchen.link_room(hall,"south")
living_room.link_room(hall,"east")

kitchen.link_room(utility_room,"north")
utility_room.link_room(kitchen,"south")

garden.link_room(utility_room,"west")
utility_room.link_room(garden,"east")

teen_room.link_room(landing,"east")
child_room.link_room(landing,"north")
bathroom.link_room(landing,"south")
main_bedroom.link_room(landing,"west")

#items
gin = Item ("gin")
gin.set_description("A delicious nectar made with distilled spirits, juniper and botanicals. Defintely not mother's ruin.")

stitch = Item ("stitch")
stitch.set_description("The cutest little alien you ever did see. A child's best friend.")

board_game = Item ("a board game")
board_game.set_description("Stylish artwork, multitude of pieces, instruction novel - a nerd's dream")

parmo = Item ("parmo")
parmo.set_description("Someone seems to have made a pizza but has used chicken instead of bread. Beloved by teen(ish)s.")

book = Item ("book")
book.set_description ("The Big Baddie Beastiery")

plunger = Item ("plunger")
plunger.set_description ("It looks like it might have fallen off of a Dalek. Used to remove horrible things.")

tissue = Item ("tissue")
tissue.set_description("A small piece of paper but in the right hands it could be deadly.")

#characters
dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("Braiiiinnnnss!!")
dave.set_weakness ("plunger")

aragog= Enemy("Aragog", "A giant spider - there is definitely drool")
aragog.set_conversation("Attercop, Attercop")
aragog.set_weakness ("tissue")


child = Friend("Child", "A bright and chirpy young man playing a Nintendo Switch.")
child.set_conversation ("Did you know that Pikachu can use Electroweb and it can cause the enemy to be trapped. It is especially strong against water types and you can tell they are a girl because their tail is a heart")
child.set_hug_description ("puts the Nin down and says 'I love you' and gives you a great big hug. He then picks up the Nin and goes back to hunting Pokemon")
child.set_gift ("stitch")
child.set_receive_description ("Yaaay, It's Stitchy. He puts the Nin down and gives Stitch a big hug.")

teen = Friend ("Teen-ish", "A girl who is smart, clever and funny. But also messy. Is probably watching Youtube.")
teen.set_conversation  ("Ungh!")
teen.set_hug_description  ("smiles. Despite looking like she might bite your head off, she gives you a lovely hug.")
teen.set_gift("parmo")
teen.set_receive_description("Thanks! Nom, Nom, Nom, Nom!")

mum = Friend ("Mum", "An astounding woman who creates masterpieces both of arts and living things.")
mum.set_conversation ("Get in the bin!")
mum.set_hug_description ("gives the kind of hug that makes everything seem better.")
mum.set_gift("gin")
mum.set_receive_description ("Thanks I really needed that")

dad = Friend ("Dad","Bald, glasses, geek, a little grumpy. What more could you want?")
dad.set_conversation ("starts talking about some science thing. You pay no attention")
dad.set_hug_description("gives a great big hug (but is still a nerd)")
dad.set_gift("popcorn")
dad.set_receive_description("Thanks. He opens the box and starts rolling random dice and asking if anyone wants to trade sheep for brick.")

#inhabitant (starting positions)
dining_room.set_character(dave)
hall.set_character(aragog)

living_room.set_character (child)
teen_room.set_character(teen)
main_bedroom.set_character(mum)
garden.set_character(dad)


#item locations

kitchen.set_item (parmo)
hall.set_item (gin)
child_room.set_item (stitch)
dining_room.set_item(board_game)
landing.set_item(book)
bathroom.set_item(plunger)
utility_room.set_item(tissue)

#starting room
old_room=dining_room
current_room = kitchen

game_over = False

cambridge = RPGInfo("An unassuming house")
cambridge.welcome()
RPGInfo.info()


##print("There are " + str(Room.number_of_rooms) + " rooms to explore.")
##print ("There are " + str(Friend.number_of_friends) + " friends left to help")

##checks to see if game has reached a game end state.

while not(game_over):

## check to see if movement has occurred and if so print details of new room.

    if current_room == old_room:
        print()
    else:

        print()
        current_room.get_details()
        inhabitant = current_room.get_character()
        if inhabitant is not None:
            print()
            inhabitant.describe()
        room_item = current_room.get_item()
        if room_item is not None:
            item_name = room_item.get_name
            print ()
            print ("You also see: ", item_name())


## contains instructions for command line entries.
    old_room=current_room
    command = input("> ").lower()
    if command == "quit":
        print("Game Over\nPlease return again some day\n")
        game_over = True
    elif command in ["north", "south", "east", "west","up","down"]:
        current_room = current_room.move(command)
    elif command == "talk":
        if inhabitant is not None:
            print()
            talk(inhabitant)
        else:
            print ("I really hope that you are not expecting an answer!")

## check whether an inhabitant is present before fighting.

    elif command == "fight":
        if inhabitant is not None:
            if isinstance(inhabitant,Enemy):
                if fight (inhabitant)==True:
                    game_over=True
                else:
                    current_room.set_character(None)

            else:
                print ("They refuse to fight you")
        else:
            print ("This is not Fight Club you know!")

## check whether there is an inhabitant and whether it is friendly.

    elif command == "hug":
        if inhabitant is not None:
            if isinstance(inhabitant, Friend):
                hug (inhabitant)
            else:
                print ("You lean in for a hug and your throat is torn out. Game Over!")
                game_over=True

## check whether an object is present and whether there is an enemy guarding it.

    elif command == "take":
        if room_item is not None:
            if isinstance(inhabitant, Enemy):
                print ("You would take the item but the ", inhabitant.name, " is pretty scary and you can't while it is here")

            else:
                item_name = room_item.get_name()
                take (item_name)

        else:
            print ("You reach forward for the item before realising that you are hallucinating. I recommend more sleep.")

## redescribe room
    elif command == "look":
        current_room.get_details()

## list picked up items
    elif command == "inventory":
        print ("You are carrying: ", [backpack])
## examines any items in the room (for ease at present it only assumes one object)
    elif command == "examine":
        if room_item is not None:
            room_item.get_details()
        else:
            print ("No matter how hard you look you do not see any more detail in the nothing that is here!")

    ## checks to see whether there is an inhabitant and whether it is a friend.

    elif command == "give":
        if inhabitant is not None:
            if isinstance (inhabitant, Enemy):
                print ("I don't think you should do that!!")
            else:
                if give (inhabitant) == True:
                    game_over = True
        else:
            print ("There is nobody here to receive your gift.")

    ## single object command for the book of beasties. Gives clues to killing enemies

    elif command == "read":
        if room_item is not book:
            print ("Erm...there is nothing to read here")
        else:
            print ("The book says to kill a Zombie, you need to take the plunge. Sneezy can slay spiders.")

## lists commands that are available.

    elif command == "help":
        RPGInfo.commands()
    else:
        print ("I don't understand what you mean")

RPGInfo.author = "willsy24"
RPGInfo.credits()

class Character():

    # Create a character
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

    # Describe this character
    def describe(self):
        print( self.name + " is here!" )
        print( self.description )

    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        self.conversation = conversation

    # Talk to this character
    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    # Fight with this character
    def fight(self, combat_item):
        print(self.name + " doesn't want to fight with you")
        return True# Write your code here :-)

class Enemy(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None
    def set_weakness(self, weakness):
        self.weakness = weakness
    def get_weakness(self, weakness):
        return self.weakness

    ## checks to see if correct weapon is being used. Either sets victory (return false)
    ## or loss (return True)
    def fight (self, combat_item):
        if combat_item() == self.weakness:
            print("You fend ", self.name , " off with the ", combat_item() )

            return False
        else:
            print(self.name, " crushes you, puny adventurer. ")
            print("You have died. Game Over")
            return True

## add Friend sub class. has 2 methods hug and give. Also tracks victory using happy and number_of_friends
## variable. When these are equal the game is complete.

class Friend(Character):
    happy = 0
    number_of_friends = 0
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        Friend.number_of_friends = Friend.number_of_friends + 1

    def set_gift(self, gift):
        self.gift = gift
    def get_gift (self, gift):
        self.gift
    def set_hug_description(self, hug_description):
        self.hug_description = hug_description
    def get_hug_decription(self, hug_description):
        return self.hug_description
    def set_receive_description(self, receive_description):
        self.receive_description = receive_description
    def get_receive_description(self, receive_description):
        return self.receive_description
    def hug (self):
        print (self.name, " ", self.hug_description)

   ## checks to see if the gift given is the gift that is wanted.
   ## adds 1 to Friend.happy.

    def give (self, gift_given):
        if gift_given()== self.gift:
           print (self.name, self.receive_description)
           Friend.happy = Friend.happy + 1
           return True
        else:
            print ("That is very kind of you but they do not want that")
            return False

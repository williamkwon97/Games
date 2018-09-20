import time

# Requirements Item: Import another Python file above - 20 pts
# Requirements Item: A Class below - 40 pts
class item():
    def __init__(self, name, actionDeclaration, intro, option_text, reaction_text, reaction_reward, success_check=False, success=False):
        # unpacks the object
        self.name = name  # Internal name of the object. Honestly, isn't used that much
        self.actionDeclaration = actionDeclaration  # The words which appear when the player enters a room
        self.intro = intro  # The intro called when the player decides to interact with the object
        self.option_text = option_text  # The text of the options presented to the player
        self.reaction_text = reaction_text  # the text when the player decides to do some action
        self.reaction_reward = reaction_reward  # the value of the rewards based on the decisions that you made.
        self.success_check = success_check
        self.success = success
        pass


    def interact(self):
        """
        Method interact is called when the player decides to interact with the object. It returns the reward for
        interacting with the object as an integer.
        """
        # Requirements Item: 2 styles of comments one above and one below - 10 pts
        # Prints the introduction of the item
        print(self.intro)
        print("#Options: ")

        # Prints the options
        for i in range(len(self.option_text)):
            print("| " + str(i+1) + ". " + self.option_text[i])

        # Block for accepting a user input
        while True:
            user_input = input("#Action: ")
            if user_input == "1" and self.success_check == True:
                self.success = True


            # sees if the user input is an int or a string
            try:
                user_input = int(user_input)
                if user_input-1 < len(self.option_text):
                    print(self.reaction_text[user_input-1])
                    return_value = self.reaction_reward[user_input-1]
                    break
                else:
                    print("#Input not understood, please try again.")
            except:
                print("#Input the number of the option, not the words")

        return return_value


class map():
    def __init__(self):
        # Declare the items in the room and navigation options
        self.rooms = []
        self.rooms.append([])  # Makes room 1
        self.rooms.append([])  # Makes room 2
        self.rooms.append([])  # Makes room 3
        self.rooms.append([])  # Makes room 4
        self.rooms.append([])  # Makes room 5
        self.rooms.append([])  # Makes room 6

        self.roomNames = ["Kitchen", "Dinning Room", "Living Room", "Brother's Room", "Father's Room", "pantry"]

        self.current_room = 0  # Needs to be a number between 1 and 6

    def moveRoom(self):

        # This controls which rooms you can move to.
        """
        rooms are arranged as such:
        room 0 | room 1 | room 2
        ------------------------
        room 5 | room 4 | room 3
        """
        if self.current_room == 0:
            room_options = [1,5]
        elif self.current_room == 1:
            room_options = [0,2,4]
        elif self.current_room == 2:
            room_options = [1,3]
        elif self.current_room == 3:
            room_options = [2,4]
        elif self.current_room == 4:
            room_options = [1,3,5]
        elif self.current_room == 5:
            room_options = [0,4]
        else:
            print("#Wow, that's weird. Anyway, we're sending back to room 0")
            room_options = [1,5]
        pass

        # ("DEBUG: Currently in room: " + str(self.current_room))

        # Prints intro to navigation
        print("You can move to one of the following rooms")
        print("#Options")

        i = 0
        for x in room_options:
            print("| " + str(i+1) + ". " + self.roomNames[x])
            i += 1

        # Accepts User input
        while True:
            user_input = input("#Answer: ")
            try:
                user_input = int(user_input)
                print(room_options)
                if user_input-1 < len(room_options):
                    print("You walk into the " + self.roomNames[room_options[user_input-1]].lower() +".")
                    self.current_room = room_options[user_input-1]  # Updates the current room of the player
                    break
                else:
                    print("#That's not an option!")
            except:
                print("#Input the number of the option, not the words")

    def currentRoomReturner(self):
        return self.current_room

    def exploreOptions(self):
        """
        looks at all the options available to the user in the room due to the items in the room, and prints them out
        """
        pass


def main():

    # this is for cool intro text - might change later - look at comment below

    # If you want a new file to do something else with
    # DO NOT USE THE SAME TXT FILE CREATE A NEW ONE ~~~~~~!!!!!!!!!!!!!

    print("Brought to you by:")
    time.sleep(2)
    # Requirements Item:file reading below - 35 pts
    TxtFile1 = open("txt1.txt", "r")
    for x in TxtFile1:
        if x != "stop\n":
            print(x.strip("\n"))
        else:
            break
    time.sleep(1)
    # this is just a you know a press start to play the game scene
    pressToPlay = input("\nTo play the dinner part scene hit enter: ")
    print("\nBackground Story:\n")
    # I might enter a save state option here
    # we need an introduction manual somewhere
    # Requirements Item: For loop below - 15 pts
    for x in TxtFile1:
        if x != "stop\n":
            print(x.strip("\n"))

        else:
            break
    time.sleep(2)
    TxtFile1.close()

    pressToPlay = input("\nHit enter after reading plot to go deal with the guests: ")

    # ITEM called Stephen
    stephen_name = "Stephen"
    stephen_actionDeclaration = "Talk to Stephen"
    stephen_intro = "Hello, I,m just going to be candid. My vote is going to your brother and you can't change my mind."
    stephen_option_text = ("Poison","Bribe","Walk away")
    stephen_R1 = "Stephen is allergic to peanuts, go get peanuts from pantry"
    stephen_R2 = "Stephen goes into anaphylactic shock. After recovering himself with his epipen, he leaves on account of being tired."
    stephen_reaction_text = [stephen_R1, "Stephen looks confused and rejects the bribe", "Darn, you probably could have poison him"]
    stephen_reaction_reward = (0,0,0)

    item_stephen = item(stephen_name, stephen_actionDeclaration, stephen_intro, stephen_option_text, stephen_reaction_text, stephen_reaction_reward)

    # ITEM called shelf
    shelf_name = "shelf"
    shelf_actionDecleration = "Look at the shelves' contents"
    shelf_intro = "There are peanuts on one of the shelves"
    shelf_option_text = ("Take Peanuts", "Take a considerable amount of Peanuts")
    shelf_reaction_text = ["You stored the peanuts in your inventory", "You stored the peanuts in your inventory"]
    shelf_reaction_reward = (0, 0)
    item_shelf = item(shelf_name, shelf_actionDecleration, shelf_intro, shelf_option_text,
                        shelf_reaction_text, shelf_reaction_reward)

    # ITEM called Sophia
    sophia_name = "Sophia"
    sophia_actionDecleration = "Talk with Sophia"
    sophia_intro = "I can be persuaded into giving you my vote tonight, but it'd cost you a pretty penny."
    sophia_option_text = ("Bribe", "Poison", "Walk Away")
    sophia_R1 = "Sophia needs money, you don't have money"
    sophia_R2 = "You now have Sophia's vote!"
    sophia_reaction_text = [sophia_R1, "Sophia is not allergic to peanuts", "Darn, you probably could have bribed her"]
    sophia_reaction_reward = (0, 0, 0)

    item_sophia = item(sophia_name, sophia_actionDecleration, sophia_intro, sophia_option_text, sophia_reaction_text,
                       sophia_reaction_reward)

    # ITEM called drawer
    drawer_name = "drawer"
    drawer_actionDecleration = "Look at the drawer' contents"
    drawer_intro = "There is money in the drawer"
    drawer_option_text = ("Take money", "Take quite a bit of money")
    drawer_reaction_text = ["You stored the money in your inventory", "You stored the money in your inventory"]
    drawer_reaction_reward = (0, 0)

    item_drawer = item(drawer_name, drawer_actionDecleration, drawer_intro, drawer_option_text,
                       drawer_reaction_text, drawer_reaction_reward)

    # ITEM called Sean
    sean_name = "Sean"
    sean_actionDecleration = "Talk with Sean"
    sean_intro = "I am loyal to your father and thus I am loyal to your brother."
    sean_option_text = ("Blackmail", "Bribe", "Poison", "Walk Away")
    sean_R1 = "Your father may have something on me, but you don't!"
    sean_R2 = "You now have Sean's vote!"
    sean_reaction_text = [sean_R1, "There are things more valuable than money like secrets",
                            "Sean is not allergic to peanuts", "Darn, you probably could have blackmailed him"]
    sean_reaction_reward = (0, 0, 0, 0)

    item_sean = item(sean_name, sean_actionDecleration, sean_intro, sean_option_text, sean_reaction_text,
                       sean_reaction_reward)

    # ITEM called desk
    desk_name = "desk"
    desk_actionDecleration = "Look at the desk' contents"
    desk_intro = "There is a mysterious paper on the desk"
    desk_option_text = ("Take mysterious paper", "Take mysterious paper")
    desk_reaction_text = ["You stored the mysterious paper in your inventory",
                          "You stored the mysterious paper in your inventory"]
    desk_reaction_reward = (0, 0)

    item_desk = item(desk_name, desk_actionDecleration, desk_intro, desk_option_text,
                     desk_reaction_text, desk_reaction_reward)
    # EXAMPLE of interacting with stephen
    # item1.interact()


    # Game Begins Below
    game_map = map()
    user_inventory = set([""])

    while True:
        currentRoom = game_map.currentRoomReturner()
        # what can happen in room 0
        if item_stephen.success == True and item_sophia.success == True and item_sean.success == True:
            print("************************************************************************************************")
            print("************************************************************************************************")
            print("Congratulations, you have dealt with all the significant members on the board of the director's"
                  " before the vote.\n Therefore, you are now the proud CEO of your father's company.\n You will "
                  "forever remember the look on your father's face when you won.\n")
            final_user_action = input("Press enter to end game:")
            break
        elif currentRoom == 0:
            user_room_move_check = 0
            while user_room_move_check == 0:
                print("In this room is Stephen")
                user_action_choice = input("What do you wish to do:\n")

                if user_action_choice.upper() == "MOVE ROOMS":
                    game_map.moveRoom()
                    user_room_move_check = 1
                elif user_action_choice.upper() == "INTERACT WITH STEPHEN":
                    if item_stephen.success == True:
                        print("Stephen has already left, are you imagining him out of guilt?")
                    elif "peanuts" in user_inventory:
                        stephen_reaction_text[0] = stephen_R2
                        item_stephen.interact()
                        item_stephen.success_check = True

                    elif "peanuts" not in user_inventory:
                        item_stephen.interact()
                else:
                    print("Not a valid option: Either \"interact with _____\" or \"move rooms\"")
        # what can happen in room 1
        elif currentRoom == 1:
            user_room_move_check = 0
            while user_room_move_check == 0:
                print("In this room is Sophia")
                user_action_choice = input("What do you wish to do:\n")

                if user_action_choice.upper() == "MOVE ROOMS":
                    game_map.moveRoom()
                    user_room_move_check = 1

                elif user_action_choice.upper() == "INTERACT WITH SOPHIA":
                    if item_sophia.success == True:
                        print("You already have Sophia's vote!")
                    elif "money" in user_inventory:
                        sophia_reaction_text[0] = sophia_R2
                        item_sophia.interact()
                        item_sophia.success_check = True

                    elif "money" not in user_inventory:
                        item_sophia.interact()

                else:
                    print("Not a valid option: Either \"interact with _____\" or \"move rooms\"")
        # what can happen in room 2
        elif currentRoom == 2:
            user_room_move_check = 0
            while user_room_move_check == 0:
                print("In this room is Sean")
                user_action_choice = input("What do you wish to do:\n")

                if user_action_choice.upper() == "MOVE ROOMS":
                    game_map.moveRoom()
                    user_room_move_check = 1

                elif user_action_choice.upper() == "INTERACT WITH SEAN":
                    if item_sean.success == True:
                        print("You already have Sean's vote!")
                    elif "paper" in user_inventory:
                        sean_reaction_text[0] = sean_R2
                        item_sean.interact()
                        item_sean.success_check = True

                    elif "paper" not in user_inventory:
                        item_sean.interact()
                # where to put other interactions
                #  e.g. elif user_action_choice.upper() == "INTERACT WITH STEPHEN":

                else:
                    print("Not a valid option: Either \"interact with _____\" or \"move rooms\"")
        # what can happen in room 3
        elif currentRoom == 3:
            user_room_move_check = 0
            while user_room_move_check == 0:
                print("In this room is an interesting drawer")
                user_action_choice = input("What do you wish to do:\n")

                if user_action_choice.upper() == "MOVE ROOMS":
                    game_map.moveRoom()
                    user_room_move_check = 1

                elif user_action_choice.upper() == "INTERACT WITH DRAWER" or \
                        user_action_choice == "INTERACT WITH INTERESTING DRAWER":
                    item_drawer.interact()
                    user_inventory.add("money")
                # where to put other interactions
                #  e.g. elif user_action_choice.upper() == "INTERACT WITH STEPHEN":

                else:
                    print("Not a valid option: Either \"interact with _____\" or \"move rooms\"")
        # what can happen in room 4
        elif currentRoom == 4:
            user_room_move_check = 0
            while user_room_move_check == 0:
                print("In this room is a grand desk")
                user_action_choice = input("What do you wish to do:\n")

                if user_action_choice.upper() == "MOVE ROOMS":
                    game_map.moveRoom()
                    user_room_move_check = 1

                elif user_action_choice.upper() == "INTERACT WITH DESK" or \
                        user_action_choice == "INTERACT WITH GRAND DESK":
                    item_desk.interact()
                    user_inventory.add("paper")

                # where to put other interactions
                #  e.g. elif user_action_choice.upper() == "INTERACT WITH STEPHEN":

                else:
                    print("Not a valid option: Either \"interact with _____\" or \"move rooms\"")
        # what can happen in room 5
        elif currentRoom == 5:
            user_room_move_check = 0
            while user_room_move_check == 0:
                print("In this room is a shelf")
                user_action_choice = input("What do you wish to do:\n")

                if user_action_choice.upper() == "MOVE ROOMS":
                    game_map.moveRoom()
                    user_room_move_check = 1

                elif user_action_choice.upper() == "INTERACT WITH SHELF":
                    item_shelf.interact()
                    user_inventory.add("peanuts")
                # where to put other interactions
                #  e.g. elif user_action_choice.upper() == "INTERACT WITH STEPHEN":

                else:
                    print("Not a valid option: Either \"interact with _____\" or \"move rooms\"")


main()
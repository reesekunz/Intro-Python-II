from room import Room
from player import Player
from item import Item

# attack items = sword, bow, spear (item_name, item_description, attack_level) -> from Attack class attributes
# defense items = shield, helmet (item_name, item_description, defense_level) -> from Defense class attributes
# magic items = staff, wand (item_name, item_description, magic_level) -> from Magic class attributes
# health items = potion, food (item_name, item_description, health_level) -> from Health class attributes
item = {
    # "any name": Class Being Referenced("attribute 1 inside class", "atrribute 2 inside class", "attribute 3 inside class")
    "sword": Attack("Wildling sword", "Increases attack level by 3", 4),
    "bow": Attack("bow & arrow", "Increases attack level by 2", 3),
    "spear": Attack("wimpy spear", "Increases attack level by 1", 1),
    "shield": Defense("Strong shield", "Increases defense level by 4", 4),
    "helmet": Defense("Broken helmet", "Increases defense level by 2", 2),
    "staff": Magic("magic staff", "Increases magic level by 2", 2),
    "wand": Magic("Harry Potters wand", "Yur a wizard Harry. Increaes magic level by 5", 5),
    "potion": Health("HP potion", "Restores health level by 30", 30),
    "food": Health("Food", "Restores health level by 10", 10)
}

# Declare all the rooms
room = {
    # "any name": Class Being Referenced("attribute 1 inside class", "atrribute 2 inside class")
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
# player_name = input("Input player name")
player = Player("Reese", room["outside"])
# Write a loop that:

# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
nogo = "Can't go that way"

# def move():
while True:
    # define input
    key = input(
        "Welcome to our adventure game! Press 'n' to go north, 's' for south, 'e' for east, 'w' for west, or 'q' to quit ")
    # REPL should accept "n", "s,", "e", "w", "q" commands
    possible_inputs = ['n', 's', 'e', 'w', 'q']
    # Verify its one of the possible key entries
    if key not in possible_inputs:
        print("Not a valid key input, please enter: 'n', 's', 'e', 'w', or 'q'")
    # North
    elif key == "n":
        # None is what is declared in room.py
        if player.current_room.n_to == None:
            print(nogo)
        else:
            move_player = player.current_room.n_to
            print(move_player)
    # South
    elif key == "s":
        if player.current_room.s_to == None:
            print(nogo)
        else:
            move_player = player.current_room.s_to
            print(move_player)
    # East
    elif key == "e":
        if player.current_room.e_to == None:
            print(nogo)
        else:
            move_player = player.current_room.e_to
            print(move_player)
    # West
    elif key == "w":
        if player.current_room.w_to == None:
            print(nogo)
        else:
            move_player = player.current_room.w_to
            print(move_player)

    # Quit
    elif key == "q":
        # Break out of loop
        print("Thanks for playing!")
        break


# move()

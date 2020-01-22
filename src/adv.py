from room import Room
from player import Player
# Declare all the rooms

room = {
    # "any name": Class Being Referenced("attribute 1 inside class" - room_name, "atrribute 2 inside class" - room_description)
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
player = Player("Reese", room["outside"])
print(player)


# PLANNING
# If the user enters a cardinal direction, attempt to move to the room there.
# carindal direction inputs = n, s, e, w
# valid inputs = n, s, e, w, q
# if key isnt a valid input, print an error
# If the user enters "q", quit the game.

while True:
    key = input(
        "Welcome! To get started press 'n' to go north, 's' for south, 'e' for east, 'w' for west, or 'q' to quit ")
    possible_inputs = ['n', 's', 'e', 'w', 'q']

    if key not in possible_inputs:
        print("Not a valid key input, please enter: 'n', 's', 'e', 'w', or 'q'")
# North
    elif key == "n":
        # Can either not go more north
        if player.current_room.n_to == None:
            print("Cant go that way")
        # Or can go north to another room
        else:
            room = player.current_room.n_to
            print(room)
# South
    elif key == "s":
        # Can either not go more south
        if player.current_room.s_to == None:
            print("Cant go that way")
        # Or can go north to another room
        else:
            next_room = player.current_room.s_to
            print(next_room)
# East
    elif key == "e":
        if player.current_room.e_to == None:
            print("Cant go that way")
        else:
            next_room = player.current_room.e_to
            print(next_room)
# West
    elif key == "w":
        if player.current_room.w_to == None:
            print("Cant go that way")
        else:
            next_room = player.current_room.w_to
            print(next_room)
# Quit
    elif key == "q":
        print("Bye bye")
        break  # Break out of loop

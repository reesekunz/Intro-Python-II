from room import Room
from player import Player
# Declare all the rooms

room = {
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


# def move():
while True:  # Loop
        # Read
    key = input("-> ")

    possible_inputs = ['n', 's', 'e', 'w', 'q']
    #
    if key not in possible_inputs:
        print("Not a valid key input, please enter: 'n', 's', 'e', 'w', or 'q'")
    # North
    elif key == "n":
        if player.current_room.n_to == None:
            print("Can't go that way")
        else:
            move_player = player.current_room.n_to
            print(move_player)
    # South
    elif key == "s":
        if player.current_room.s_to == None:
            print("Can't go that way")
        else:
            move_player = player.current_room.s_to
            print(move_player)
    # East
    elif key == "e":
        if player.current_room.e_to == None:
            print("Can't go that way")
        else:
            move_player = player.current_room.e_to
            print(move_player)
    # West
    elif key == "w":
        if player.current_room.w_to == None:
            print("Can't go that way")
        else:
            move_player = player.current_room.w_to
            print(move_player)

    # Quit
    elif key == "q":
        # Break out of loop
        print("Thanks for playing!")
        break


# move()
# Verify its one of the possible key entries

# REPL should accept "n", "s,", "e", "w", "q" commands

# Write a loop that:

# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.

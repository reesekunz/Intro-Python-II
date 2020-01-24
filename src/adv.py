from room import Room
from player import Player
from item import Item, Attack, Defense, Magic, Health
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

# Make a new player object that is currently in the 'outside' room.
player = Player("Reese", room["outside"])
# Reese is currently in Room: Outside Cave Entrance. Room description: North of you, the cave mount beckons
print("player", player)

# Room: Outside Cave Entrance. Room description: North of you, the cave mount beckons
# print("player.current_room", player.current_room)
# print("player.player_name", player.player_name)  # Reese
# print("player.current_room.room_name",
#       player.current_room.room_name)  # Outside Cave Entrance
# print("player.current_room.room_description",
#       player.current_room.room_description)  # North of you, the cave mount beckons

while True:
    key = input(
        "Press 'n' to go north, 's' for south, 'e' for east, 'w' for west, or 'q' to quit")
    possible_inputs = ['n', 's', 'e', 'w', 'q']

    if key not in possible_inputs:
        print("Not a valid key input, please enter: 'n', 's', 'e', 'w', or 'q'")
# North
    elif key == "n":
        if player.current_room.n_to is not None:
            player.current_room = player.current_room.n_to
            print("***player.current_room***", player.current_room)
        else:
            print("Cant go that way")


# South
    elif key == "s":
        if player.current_room.s_to is not None:
            player.current_room = player.current_room.s_to
            print("***player.current_room***", player.current_room)
        else:
            print("Cant go that way")


# East
    elif key == "e":
        if player.current_room.e_to is not None:
            player.current_room = player.current_room.s_to
            print("***player.current_room***", player.current_room)
        else:
            print("Cant go that way")

# West
    elif key == "w":
        if player.current_room.w_to is not None:
            player.current_room = player.current_room.w.to
            print("***player.current_room***", player.current_room)
        else:
            print("Cant go that way")


# Quit
    elif key == "q":
        print("Bye bye")
        break  # Break out of loop

from room import Room
from player import Player
from item import Item, Attack, Defense, Magic, Health

# Declare items
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

# Link items to rooms
room['outside'].room_items = item["sword"]
room['outside'].room_items = item["shield"]
room['foyer'].room_items = item["bow"]
room['foyer'].room_items = item["staff"]
room['overlook'].room_items = item["spear"]
room['overlook'].room_items = item["wand"]
room['narrow'].room_items = item["shield"]
room['narrow'].room_items = item["potion"]
room['treasure'].room_items = item["helmet"]

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
    possible_inputs = ['n', 's', 'e', 'w', 'q', 'i']

    if key not in possible_inputs:
        print("Not a valid key input, please enter: 'n', 's', 'e', 'w', 'q', or 'i")
# North
    elif key == "n":
        if player.current_room.n_to is not None:
            player.current_room = player.current_room.n_to
            print("***player.current_room***", player.current_room)
            print("Press 'i' to inspect room for items")
        else:
            print("Cant go that way")


# South
    elif key == "s":
        if player.current_room.s_to is not None:
            player.current_room = player.current_room.s_to
            print("***player.current_room***", player.current_room)
            print("Press 'i' to inspect room for items")
        else:
            print("Cant go that way")


# East
    elif key == "e":
        if player.current_room.e_to is not None:
            player.current_room = player.current_room.s_to
            print("***player.current_room***", player.current_room)
            print("Press 'i' to inspect room for items")
        else:
            print("Cant go that way")

# West
    elif key == "w":
        if player.current_room.w_to is not None:
            player.current_room = player.current_room.w.to
            print("***player.current_room***", player.current_room)
            print("Press 'i' to inspect room for items")
        else:
            print("Cant go that way")


# Quit
    elif key == "q":
        print("Bye bye")
        break  # Break out of loop

# Inspect room for items
    elif key == "i":
        print(f'You found: {player.current_room.room_items}')

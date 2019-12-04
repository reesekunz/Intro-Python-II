# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, player_name, room):
        self.player_name = player_name
        self.room = room

    def __str__(self):
        return f"{self.player_name} is currently in room {self.room}"

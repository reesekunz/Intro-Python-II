# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, room, description):
        self.room = room
        self.description = description
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None

    def __str__(self):
        return f"room: {self.room} description: {self.description}"

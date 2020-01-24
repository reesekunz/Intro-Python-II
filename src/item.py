# Item class to hold item information

# General item (base) class who's attributes (item name and item description) will be passed down to the item classes below


class Item:
    def __init__(self, item_name, item_description):
        self.item_name = item_name
        self.item_description = item_description

    def __str__(self):
        return f"Item: {self.item_name} Description: {self.item_description}"

# Specific items we want to inherent the item attributes above - sword, shield, staff, potion

# Sword


class Attack(Item):
    def __init__(self, item_name, item_description, attack_level):
        # Use super() to inherent item class attributes above
        super().__init__(item_name, item_description)
        # Add on whatever specific attributes are missing from parent class
        self.attack_level = attack_level

    def __str__(self):
        return f"Item: {self.item_name} Description: {self.item_description} Increases attack level by: {self.attack_level}"

# Shield


class Defense(Item):
    def __init__(self, item_name, item_description, defense_level):
        super().__init__(item_name, item_description)
        self.defense_level = defense_level

    def __str__(self):
        return f"Item: {self.item_name} Description: {self.item_description} Increases defense level by: {self.defense_level}"

# Staff


class Magic(Item):
    def __init__(self, item_name, item_description, magic_level):
        super().__init__(item_name, item_description)
        self.magic_level = magic_level

    def __str__(self):
        return f"Item: {self.item_name} Description: {self.item_description} Increases magic level by: {self.magic_level}"

# Potion


class Health(Item):
    def __init__(self, item_name, item_description, health_level):
        super().__init__(item_name, item_description)
        self.health_level = health_level

    def __str__(self):
        return f"Item: {self.item_name} Description: {self.item_description} Increases health level by: {self.health_level}"

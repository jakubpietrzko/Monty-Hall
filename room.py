import random
from door import Door

# Class representing a room with three doors
class Room:
    def __init__(self):
        self.door_a = Door(None)
        self.door_b = Door(None)
        self.door_c = Door(None)
        self.shuffle_contents()
    
    def shuffle_contents(self):
        # Randomly assigns two goats and one car behind the three doors
        contents = ["goat", "goat", "car"]
        random.shuffle(contents)
        self.door_a.content = contents[0]
        self.door_b.content = contents[1]
        self.door_c.content = contents[2]
    
    def choose_door(self, index):
        # Returns the door corresponding to the given index (0, 1, or 2)
        if index == 0:
            return self.door_a
        elif index == 1:
            return self.door_b
        elif index == 2:
            return self.door_c
        else:
            raise ValueError("Invalid door index")
    
    def open_goat_door(self, chosen_index):
        # Selects and returns the index of a door with a goat that wasn't chosen by the player
        available_doors = [i for i in range(3) if i != chosen_index and self.choose_door(i).content == "goat"]
        return random.choice(available_doors)
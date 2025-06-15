import random

# Class representing a single door
class Door:
    def __init__(self, content):
        self.content = content
    
    def __str__(self):
        return self.content
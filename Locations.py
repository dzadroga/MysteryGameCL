# Base file for all location instances in the game
#Created on 11/20/2026

class Location:

    def __init__(self, name, description, clues):
        self.name = name
        self.description = description
        self.clues = clues

    def getClues(self, locationClues):
        return self.clues.get(locationClues, "I am not seeing anything here")
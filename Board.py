from operator import ne
import random

"""
A class representing the board of the game.
Contains lists of units and their locations
"""

class Board():
    def __init__(self, initial_conditions):
        """
        Initializes the board.

        Parameters
        ----------
        initial_conditions : {'units': [Unit, Unit, ...],
                                'locations': [(int, int), (int, int), ...].
                                'dimensions': (int, int)}
        """

        self.units = initial_conditions['units']
        self.locations = initial_conditions['locations']
        self.DIMENSIONS = initial_conditions['dimensions']
    
    def move_units(self):
        for i, location in enumerate(self.locations):
            for j in range(int(self.units[i].speed)):
                location = ((location[0] + random.randint(-1, 1))%self.DIMENSIONS[0], (location[1] + random.randint(-1, 1))%self.DIMENSIONS[1])


    def find_matches(self):
        matches = []
        for i, location in enumerate(self.locations):
            iter = i
            while self.locations[(iter + 1):].count(location) > 0:
                next_iter = self.locations[iter:].index(location)
                matches.append((iter, next_iter))
                iter = next_iter
        return matches
    
    def execute_action(self, matches):
        for match in matches:
            unit_a = self.units[match[0]]
            unit_b = self.units[match[1]]
            if unit_a.species == unit_b.species and unit_a.gender != unit_b.gender:
                new_unit = unit_a.breed(unit_b)
                self.units.append(new_unit)
                self.locations.append(self.locations[match[0]])
            else:
                outcome = unit_a.attack(unit_b)
                if outcome[0] == False and outcome[1] == False:
                    self.units.pop(match[0])
                    self.units.pop(match[1] - 1)
                    self.locations.pop(match[0])
                    self.locations.pop(match[1] - 1)
                elif outcome[0] == False:
                    self.units.pop(match[0])
                    self.locations.pop(match[0])
                elif outcome[1] == False:
                    self.units.pop(match[1])
                    self.locations.pop(match[1])
    
    def next_turn(self):
        self.move_units
        self.execute_action(self.find_matches)


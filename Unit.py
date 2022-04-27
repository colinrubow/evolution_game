from scipy import stats
import random

"""
A class representing a Unit in the game
"""

class Unit():
    def __init__(self, species, color, strength, health_max, health, gender, speed, sigma):
        """
        Initializes the Unit object.

        Parameters
        ----------
        species : string
        color : (float, float, float)
            RGB color
        strength : float
        health_max : float
        health : float
            The current health
        gender : bool
            1 is male, 0 is female
        speed : int
            A rate of blocks/turn
        sigma : float
            The randomness measure of a breed
        """
        self.species = species
        self.color = color
        self.strength = strength
        self.health_max = health_max
        self.health = health
        self.gender = gender
        self.speed = speed
        self.sigma = sigma
    
    def attack(self, opponent):
        """
        Implementation of an attack. A Unit loses health by the following
        formula -> health -= opponent.strength - (opponent.health_max/2 - opponenet.health) if opponent.health < opponenet.health_max/2 else opponenet.strength

        Parameters
        ----------
        opponent : Unit

        Returns
        -------
        A boolean duple (bool, bool) represnting self and opponenet are still alive (true) or not (false).
        """
        damage_to_self = opponent.strength - (opponent.health_max/2 - opponent.health) if opponent.health < opponent.health_max/2 else opponent.strength
        damage_to_opponenet = self.strength - (self.health_max/2 - self.health) if self.health < self.health_max/2 else self.strength
        self.health -= damage_to_self
        opponent.health -= damage_to_opponenet

        return (self.health > 0, opponent.health > 0)

    def breed(self, mate):
        """
        Implementation of a breed. A new Unit is created with shared attributes and randomness determined by a normal distribution with spread sigma.

        Parameters
        ----------
        mate : Unit

        Returns
        -------
        A new Unit. The child.
        """
        sigma_new = stats.normal.rvs(loc=(self.sigma + mate.sigma)/2, scale=(self.sigma + mate.sigma)/2, size=1)[0]
        color_new = (stats.normal.rvs(loc=(self.color[0] + mate.color[0])/2, scale=sigma_new, size=1)[0], 
                    stats.normal.rvs(loc=(self.color[1] + mate.color[1])/2, scale=sigma_new, size=1)[0],
                    stats.normal.rvs(loc=(self.color[2] + mate.color[2])/2, scale=sigma_new, size=1)[0])
        strength_new = stats.normal.rvs(loc=(self.strength + mate.strength)/2, scale=sigma_new, size=1)[0]
        health_max_new = stats.normal.rvs(loc=(self.health_max + mate.helath_max)/2, scale=sigma_new, size=1)[0]
        gender_new = random.randint(0, 1)
        speed_new = int(stats.normal.rvs(loc=(self.speed + mate.speed)/2, scale=sigma_new, size=1)[0])
        return Unit(self.species, color_new, strength_new, health_max_new, health_max_new, gender_new, speed_new, sigma_new)



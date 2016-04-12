#File: Death.py
#Author: Alexander Wu
#Purpose: Implements the death scene a player enters upon failure/death.

from sys import exit
from random import randint
from Scene import Scene


class Death(Scene):

    statements = [
      "MAN WHAT IS WRONG WITH YOU JESUS YOU FAILED",
      "MY GOD ARE YOU DUMB?! GAME OVER GAME OVER",
      "I think maybe it's time you took a break. You lose.",
      "I could fart on my keyboard and still do better than you. You have been beaten.",
      "Resistance is futile. The Borg have won. Prepare to be assimilated.",
      "You know what you are? A WEENIE. ONLY WEENIES DIE IN THIS GAME.",
      "You suck."
      
    ]

    #Upon entry of the scene, a death statement is randomly selected and the
    #game is exited.
    def enter(self, player):
        print Death.statements[randint(0, len(self.statements)-1)]
        exit(1)

from sys import exit
from random import randint
from Scene import Scene

class Death(Scene):

  statements = [ 
      "MAN WHAT IS WRONG WITH YOU JESUS"
  ]

  def enter(self):
    print Death.statements[randint(0, len(self.statements)-1)]
    exit(1)

class Player(object):

    def __init__ (self):
        self.playerName = raw_input("What is your name? ")
        self.playerInv = null                                #Placeholder, will change.
        self.playerLoc = startLoc                            #Placeholder, but this is the idea.

    def __init__ (self, name, inventory, location):
        self.playerName = name
        self.playerInv = inventory
        self.playerLoc = location



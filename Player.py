#File: Player.py
#Author: Alexander Wu
#Purpose: Implements the attributes and save functionality for character


class Player(object):

    #This constructor takes a name and sees if the save file exists.
    def __init__ (self, name):

        self.name = name 
        self.health = 0
        self.location = 'beginning'
        self.inventory = [
            False       #match          
        ]
        self.world = [
            False,          #hallway_lit
            False           #combat_cleared
        ] 
    
    #Returns player name as string
    def getName(self):
        return self.name

    #Returns player health as int
    def getHealth(self):
        return self.health

    #Allows manipulation of player health
    #Positive int when adding health, negative when removing health
    def changeHealth(self, modifier):
        self.health += modifier

    #Returns current player location as string
    def getLoc(self):
        return self.location

    #Sets player location to loc, where loc is a string.
    def setLoc(self, loc):
        self.location = loc

    #Returns item string associated with inputted index int
    def getItem( self, index ):
      return self.inventory[index]

    #Adds item to inventory 
    #index is an int
    def addItem( self, index ):
        self.inventory[index] = True
    
    #Returns boolean associated with inputted index
    #int:boolean
    def getState( self, index ):
        return self.world[index]

    #Changes state at event, where 
    #event is an int, and state is a boolean
    def changeState( self, event, state ):
        self.world[event] = state

    #Reads in save file and updates Player object
    def readSave(self, saveFile):
        self.changeHealth(int(saveFile.readline()))
        self.setLoc(saveFile.readline().splitlines()[0])
       
        #Reads in line of 0's and 1's and adds item to inventory where needed
        items = saveFile.readline().splitlines()[0]
        for i in range(0, len(self.inventory) - 1):
            if items[i] == "1":
                self.addItem(i, True) 

        #Reads in line of 0's and 1's and changes world state where needed
        events = saveFile.readline().splitlines()[0]
        for c in range(0, len(self.world) - 1):
            if events[c] == "1":
                self.changeState(c, True)

        saveFile.close()

    #Writes current player state to a file, where name is player name
    def writeSave(self):
        saveFile = open(self.name, 'w')

        saveFile.write(str(self.health) + '\n')
        saveFile.write(self.location + '\n')
      
        #Writes inventory in string of 0's and 1's. 0 indicates player
        #does not have item, and 1 indicates the player does have it
        items = ""
        for state in self.inventory:
            if state:
                items += "1"
            else:
                items += "0"
        saveFile.write(items + '\n')
        
        #Writes world state in string of 0's and 1's. 1 indicates player
        #has an item.
        items = ""
        for state in self.world:
            if state:
                items += "1"
            else:
                items += "0"
        saveFile.write(items + '\n')

        saveFile.close()

    #Prints player info
    def printInfo(self):
        print "Name: " + self.name
        print "Health: " + str(self.health)
        print "Location: " + self.location
        print "Items: ",
        for state in self.inventory:
            print state

        print "Events: ", 
        for state in self.world:
            print state

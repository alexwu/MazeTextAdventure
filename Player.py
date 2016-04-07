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

    def getName(self):
        return self.name

    def getHealth(self):
        return self.health

    #Positive when adding health, negative when removing health
    def changeHealth(self, modifier):
        self.health += modifier

    def getLoc(self):
        return self.location

    def setLoc(self, loc):
        self.location = loc

#    def printItems():
#        for item, state inventory.item()
#            if state:
#                print item
    
    def getItem( self, index ):
      return self.inventory[index]

    #item is a string
    def addItem( self, index ):
        self.inventory[index] = True
    
    #index:boolean
    def getState( self, index ):
        return self.world[index]

    def changeState( self, event, state ):
        self.world[event] = state

    def readSave(self, saveFile):
        self.changeHealth(int(saveFile.readline()))
        self.setLoc(saveFile.readline().splitlines()[0])
       
        items = saveFile.readline().splitlines()[0]
        #for c, state in zip(items, self.inventory):
        for i in range(0, len(self.inventory) - 1):
            if items[i] == "1":
                self.addItem(i, True) 

        events = saveFile.readline().splitlines()[0]
        for c in range(0, len(self.world) - 1):
            if events[c] == "1":
                self.changeState(c, True)
            #events = saveFile.readline().splitlines()

        saveFile.close()

    def writeSave(self):
        saveFile = open(self.name, 'w')

        saveFile.write(str(self.health) + '\n')
        saveFile.write(self.location + '\n')
       
        items = ""
        #for item, state in self.inventory.iteritems():
        for state in self.inventory:
            if state:
                items += "1"
            else:
                items += "0"
        
        saveFile.write(items + '\n')
        
        #for event, state in self.world.iteritems():
        items = ""
        for state in self.world:
            if state:
                items += "1"
            else:
                items += "0"

        saveFile.write(items + '\n')

        saveFile.close()

    def printInfo(self):
        print "Name: " + self.name
        print "Health: " + str(self.health)
        print "Location: " + self.location
        print "Items: ",
        for state in self.inventory:
            print state #+ '\n',

        print "Events: ", 
        for state in self.world:
            print state
        #print '\n'



class Player(object):

    #This constructor takes a name and sees if the save file exists.
    def __init__ (self, name):

        self.name = name 
        self.health = 0
        self.location = 'beginning'
        self.inventory = {}
        self.world = {
            'hallway_lit': False,
            'combat_cleared': False
        } 

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

    #item is a string
    def addItem( self, item ):
        self.inventory[item] = True
    
    #string:boolean
    def getState( self, event ):
        return self.world[event]

    def changeState( self, event, state ):
        self.world[event] = state

    def readSave(self, saveFile):
        self.changeHealth(int(saveFile.readline()))
        self.setLoc(saveFile.readline())
       
        item = saveFile.readline().splitlines()
        while item:
            self.addItem(item)
            item = saveFile.readline().splitlines()

        event = saveFile.readline().splitlines()
        while event:
            self.changeState(event, True)
            event = saveFile.readline().splitlines()

        saveFile.close()
    def writeSave(self):
        saveFile = open(self.name, 'w')

        saveFile.write(str(self.health) + '\n')
        saveFile.write(self.location + '\n')
        
        for item, state in self.inventory.iteritems():
            if state:
                saveFile.write(item + '\n')
        print ""

        for event, state in self.world.iteritems():
            if state:
                saveFile.write(event + '\n')

        saveFile.close()

    def printInfo(self):
        print "Name: " + self.name
        print "Health: " + str(self.health)
        print "Location: " + self.location
        print "Items: ",
        for item, state in self.inventory.iteritems():
            if state:
                print item + '\n',
        print '\n'



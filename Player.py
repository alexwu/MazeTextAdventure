class Player(object):

    #This constructor takes a name and sees if the save file exists.
    def __init__ (self, name):

        self.name = name 
        self.health = 0
        self.location = "beginning"
        self.inventory = {}

    def getName():
        return self.name

    def getHealth():
        return self.health

    #Positive when adding health, negative when removing health
    def changeHealth(modifier):
        self.health += modifier

    def getLoc():
        return self.location

    def setLoc(loc):
        self.location = loc

    #def getItems():
        #return inventory.item()

    #item is a string
    def addItem( item ):
        inventory[item] = True

    def writeSave():
        saveFile = open(self.name, 'w')

        saveFile.write(str(health) + '\n')
        saveFile.write(self.location)
        
        for item in inventory:
            saveFile.write(item + '\n')

    def printInfo():
        print "Name: " + self.name
        print "Health: " + self.health
        print "Location: " + self.location
        print "Items: ",
        for item in inventory:
            print item + ", ",
        print '\n'



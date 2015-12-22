class Player(object):

    #This constructor takes a name and sees if the save file exists.
    def __init__ (self, name):

        #Checks for existing save file
        if exists(name):
            #Names the Player instance
            self.playerName = name
        
            #Placeholder, should take whatever is in the file
            self.playerInv = #shit saved

            #Placeholder, but this is the idea.
            self.playerLoc = #location designated by save file
        
        else:
            self.playerName = name
            self.playerInv = #empty list (because you're starting a new game!)
            self.playerLoc = #starting location

    #When the player enters the command such as "Look around", it should refer to this funciton.
    def look (self):
        pass



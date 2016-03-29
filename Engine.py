class Engine(object):
    
    def __init__ (self, sceneMap):
        self.currentMap = sceneMap

    def play (self, player):
        #currentScene = self.currentMap.openingScene()
        currentScene = self.currentMap.nextScene(player.getLoc())
        print "Loading: " + player.getLoc()
        print currentScene
        lastScene = self.currentMap.nextScene('end')

        while currentScene != lastScene:
            nextName = currentScene.enter(player)
            currentScene = self.currentMap.nextScene(nextName)

        # If this is run, then it is the last scene of the game
        currentScene.enter(player)
        

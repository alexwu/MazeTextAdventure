class Engine(self):
    
    def __init__ (self, sceneMap):
        self.currentMap = sceneMap

    def play (self):
        currentScene = self.currentMap.openingScene()
        lastScene = self.currentMap.nextScene('end')

        while currentScene != lastScene:
            nextName = currentScene.enter()
            currentScene = self.currentMap.nextScene(nextName)

        # If this is run, then it is the last scene of the game
        currentScene.enter()
        

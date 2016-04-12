#File: Engine.py
#Author: Alexander Wu
#Purpose: The engine for the game, essentially runs the game.

class Engine(object):
    
    def __init__ (self, sceneMap):
        self.currentMap = sceneMap

    def play (self, player):
        currentScene = self.currentMap.nextScene(player.getLoc())
        lastScene = self.currentMap.nextScene('end')

        while currentScene != lastScene:
            nextName = currentScene.enter(player)
            currentScene = self.currentMap.nextScene(nextName)

        # If this is run, then it is the last scene of the game
        currentScene.enter(player)
        

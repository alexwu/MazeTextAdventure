from BeginningRoom import BeginningRoom
from Death import Death

class Map(object):

    scenes = {
            'beginning': BeginningRoom(),
            'hallway': Hallway(),
            'death': Death()
    }

    def __init__(self):
        self.startScene = 'beginning'

    def nextScene(self, scene):
        val = Map.scenes.get(scene)
        return val

    def openingScene(self):
        return self.nextScene(self.startScene)

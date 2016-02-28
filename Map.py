from BeginningRoom import BeginningRoom
from Death import Death
from Hallway import Hallway
from CombatRoom import CombatRoom


class Map(object):

    scenes = {
            'beginning': BeginningRoom(),
            'hallway': Hallway(),
            'combat': CombatRoom(),
            'death': Death()
    }

    def __init__(self):
        self.startScene = 'beginning'

    def nextScene(self, scene):
        val = Map.scenes.get(scene)
        return val

    def openingScene(self):
        return self.nextScene(self.startScene)

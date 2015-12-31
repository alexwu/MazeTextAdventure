class Map(object):

    scenes = {
            'beginning': BeginningRoom(),
    }

    def __init__(self):
        self.startScene = 'beginning'

    def nextScene(self, scene):
        val = Map.scenes.get(scene)
        return val

    def openingScene(self):
        return self.nextScene(self.startScene)

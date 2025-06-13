from gdpython import *
import random as rd

class MeinSpiel(Game):

    scene: Scene

    def start(self):
        self.backgroundLayer = Layer("background", 0, 0, -1)
        self.scene.addLayer(self.backgroundLayer)



MeinSpiel()
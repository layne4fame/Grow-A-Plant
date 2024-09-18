from flowerLibrary.flowerBad import *
from flowerLibrary.flowerGood import *
from flowerLibrary.flower import *
from flowerLibrary.leaves import *

class drawer:
    def __init__(self):
        self.baseHeight = -175
        self.iteration = 0
        self.overall = 0

    def finish(self, happy):    
        if self.overall < 6:
            drawpetalsBAD()
            drawMiddleBAD()
        elif self.overall < 9:
            drawpetals()
            drawMiddle()
        else:
            drawpetalsGOOD()
            drawMiddleGOOD()

    def drawLeaf(self, happy):
        if happy < 50:
            if self.iteration % 2 == 0:
                drawleafSadRIGHT(10, self.baseHeight)
            else:
                drawleafSadLEFT(0, self.baseHeight)
        elif happy < 75:
            self.overall = self.overall + .5
            if self.iteration % 2 == 0:
                drawleafNeutralRIGHT(10, self.baseHeight)
            else:
                drawleafNeutralLEFT(0, self.baseHeight)
        else:
            self.overall = self.overall + 1
            if self.iteration % 2 == 0:
                drawleafHappyRIGHT(10, self.baseHeight)
            else:
                drawleafHappyLEFT(0, self.baseHeight)
        if self.iteration % 2 == 1:
            self.baseHeight = self.baseHeight + 25
        self.iteration = self.iteration + 1


import flowerBad
import flowerGood
import flower
import sys
import turtle
import leaves
import background

class drawer:
    def __init__(self):
        self.baseHeight = -175
        self.iteration = 0
        self.overall = 0

    def finish(self, happy):    
        if self.overall < 6:
            flowerBad.drawpetalsBAD()
            flowerBad.drawMiddleBAD()
        elif self.overall < 9:
            flower.drawpetals()
            flower.drawMiddle()
        else:
            flowerGood.drawpetalsGOOD()
            flowerGood.drawMiddleGOOD()

    def drawLeaf(self, happy):
        if happy < 50:
            if self.iteration % 2 == 0:
                leaves.drawleafSadRIGHT(10, self.baseHeight)
            else:
                leaves.drawleafSadLEFT(0, self.baseHeight)
        elif happy < 75:
            self.overall = self.overall + .5
            if self.iteration % 2 == 0:
                leaves.drawleafNeutralRIGHT(10, self.baseHeight)
            else:
                leaves.drawleafNeutralLEFT(0, self.baseHeight)
        else:
            self.overall = self.overall + 1
            if self.iteration % 2 == 0:
                leaves.drawleafHappyRIGHT(10, self.baseHeight)
            else:
                leaves.drawleafHappyLEFT(0, self.baseHeight)
        if self.iteration % 2 == 1:
            self.baseHeight = self.baseHeight + 25
        self.iteration = self.iteration + 1


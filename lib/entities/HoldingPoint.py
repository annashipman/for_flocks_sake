from GenericBoid import GenericBoid
import random

class HoldingPoint(GenericBoid):
    def __init__(self,x,y,atlas):
        GenericBoid.__init__(self,x,y,atlas,["fountain01."+str(i) for i in range(1,70)],0)
        self.speed = 0
        self.animation_speed = 1.0
    
    def draw(self):
        self.orientation = 90
        GenericBoid.draw(self)
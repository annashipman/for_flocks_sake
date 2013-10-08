from GenericBoid import GenericBoid
import random

class Fire(GenericBoid):
    def __init__(self,x,y,atlas):
        GenericBoid.__init__(self,x,y,atlas,["fire01."+str(i) for i in range(1,20)],0)
        self.speed = 0
        self.animation_speed = 1
        self.width *= 3
        self.height *= 3
        self.update_vertices()
    
    def draw(self):
        GenericBoid.draw(self)
        GenericBoid.undraw(self)
        self.x += 2
        GenericBoid.draw(self)
        GenericBoid.undraw(self)
        self.x -= 2
        GenericBoid.draw(self)
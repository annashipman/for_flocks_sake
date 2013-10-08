from GuiString import GuiString
import random
import time

class GuiAlert(GuiString):
    def __init__(self,x,y,string,atlas,scale=1.0,easter=False):
        GuiString.__init__(self,x,y,string,atlas,scale,easter)
        if random.randint(0,1) == 0:
            self.rotation = -60
        else:
            self.rotation = 60
        self.set_alpha(0.0)
        self.start = time.time()
        self.string = string
    
    def update(self):
        GuiString.update(self)
        if abs(self.rotation) > 1.5:
           self.rotation /= 1.5
           self.set_alpha(self.get_alpha()+0.1)
        else:
            self.rotation = 0
            self.set_alpha(1.0)
    
    def alive(self):
        return time.time() - self.start < 4.0
    
    def draw(self):
        GuiString.draw(self)
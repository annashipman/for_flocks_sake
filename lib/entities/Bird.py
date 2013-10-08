from GenericBoid import GenericBoid
import random
import Particle
from State import State
from Calculations import Calculations
from GuiAnimation import GuiAnimation
from GuiSplatter import GuiSplatter

class Bird(GenericBoid):
    def __init__(self,x,y,atlas,start_frame=0):
        GenericBoid.__init__(self,x,y,atlas,["bird01.000"+str(i) for i in range(0,9)],start_frame)
        self.dying = False
        self.emitter = Particle.DeathSource(0,0,atlas)
        self.blood = None
    
    def kill(self):
        if self.dying:
            return False
        self.dying = True
        self.blood = GuiAnimation(self.x,self.y,State().atlas,["bloodExplosion01."+str(i) for i in range(0,15)],0,True)
        self.blood.width *= 2
        # if not State().splatter:
        #     State().splatter = GuiSplatter(random.randint(0,800),random.randint(0,600),State().atlas,["bloodExplosion01."+str(i) for i in range(0,16)])
        self.blood.height *= 2
        self.blood.update_vertices()
        if State().audio and Calculations().distance(self,State().player) < State().diagonal/2.0 and not State().channels[2].get_busy():
            State().music["flesh"].playSound(State().channels[2])
        return True
    
    def alternate_frames(self):
        self.keys = ["bird02.000"+str(i) for i in range(0,9)]
    
    def draw(self):
        if not self.dying:
            GenericBoid.draw(self)
        else:
            self.blood.draw()
            self.blood.undraw()
            self.emitter.draw()
    
    def undraw(self):
        if not self.dying:
            GenericBoid.undraw(self)
    
    def update(self):
        GenericBoid.update(self)
        if self.dying:
            self.blood.update()
            self.emitter.x = self.x
            self.emitter.y = self.y
            self.emitter.update()
            if self.emitter.empty():
                self.boidState = "Dead"
                self.dying = False
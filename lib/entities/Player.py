from GenericBoid import GenericBoid
from GuiColorRect import GuiColorRect
import random
import Particle
from State import State

class Player(GenericBoid):
    def __init__(self,x,y,atlas,start_frame=0):
        self.framesets = {}
        for anim in ["norm","conversion","deathEater"]:
            self.framesets[anim] = []
            for i in range(0,23):
                self.framesets[anim].append("cloudMan_"+anim+"."+str(i))
        self.current = "norm"
        GenericBoid.__init__(self,x,y,atlas,self.framesets[self.current],start_frame)
        self.emitter = Particle.Source(0,0,10,atlas)
        self.animation_speed = 1.0
    
    def update(self):
        GenericBoid.update(self)
        if self.current == "conversion" and self.frame == 0:
            self.convert("deathEater")
            State().game_screen.renderables.remove(State().point)
            State().game_screen.renderables.remove(State().player)
            State().game_screen.renderables.insert(0,State().player)
            State().game_screen.renderables.insert(0,State().point)
        self.emitter.update()
        self.emitter.x = self.x
        self.emitter.y = self.y
    
    def convert(self,string):
        self.keys = self.framesets[string]
        self.frame = 0
        self.current = string
    
    def draw(self):
        self.rotation += 90
        if self.current == "deathEater":
            self.rotation -= 180
        # self.direction = int(((self.orientation+45)/7.5)%24)
        # print self.direction
        # self.keys = self.framesets[self.direction]
        self.emitter.draw()
        GenericBoid.draw(self)
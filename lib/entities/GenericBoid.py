from GuiAnimation import GuiAnimation
import random
from Calculations import Calculations
from State import State
from math import cos, sin, radians
from GuiColorRect import GuiColorRect

class GenericBoid(GuiAnimation):
    def __init__(self,x,y,atlas,frames,start_frame):
#        GuiColorRect.__init__(self,x,y,20,20)
        GuiAnimation.__init__(self,x,y,atlas,frames,start_frame)
        
        self.orientation = random.randint(0,360)
        self.speed = 3
        self.rotation_speed = 0
        self.hit_wall_ttl = 0
        self.isCaptured = False
        self.animation_speed = random.random() + 1.0
        self.return_to_world = False
        self.isAlive = True
        self.boidState = "Normal"
        self.isInFlock = False
    
    # God damn all Java developers...
    def getPosition(self):
        return (self.x,self.y)
    
    def setPosition(self,pair):
        self.x = pair[0]
        self.y = pair[1]
    
    def getOrientation(self):
        return self.orientation
    
    def setOrientation(self,o):
        self.orientation = o
    
    def draw(self):
        if self.boidState != "Dead":
            GuiAnimation.draw(self)
            
    def undraw(self):
        if self.boidState != "Dead":
            GuiAnimation.undraw(self)
    
    def update(self):
#        if abs(self.rotation_speed) > 2 or self.frame != 8:
        self.frame += self.animation_speed
        if self.frame >= len(self.keys):
            self.frame = 0
        self.render_from_atlas(self.keys[int(self.frame)])
#        GuiColorRect.update(self)
        
        velocity = self.velocity()
        self.x += velocity[0]
        self.y += velocity[1]
        self.orientation += self.rotation_speed
        self.rotation = self.orientation + 90
    
    def velocity(self):
        return (cos(radians(self.orientation - 90)) * self.speed,sin(radians(self.orientation - 90)) * self.speed)

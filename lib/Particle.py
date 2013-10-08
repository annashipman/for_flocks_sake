import random
from State import State
import pygame
import math

from GuiSprite import GuiSprite
from GuiGroup import GuiGroup

class Particle(GuiSprite):
    def __init__(self,x,y,velocity,ttl,atlas,key="particle"):
        GuiSprite.__init__(self,x,y,atlas,key)
        self.velocity = [velocity[0],velocity[1]]
        self.ttl = ttl
        self.max_ttl = ttl
        self.type = None
        self.width = random.randint(16,24)
        self.height = self.width
        self.orig_width = self.width
        self.update_vertices()
        self.color = [random.random()/3.0+0.6,random.random()/3.0+0.3,0.0,1.0]
        self.rotation_speed = (random.random()-0.5)*2
        self.key = key
	
    def update(self):
        self.ttl -= 1
        if self.is_alive():
            self.x += self.velocity[0]
            self.y += self.velocity[1]
        self.width = float(self.ttl)/self.max_ttl*self.orig_width
        self.height = self.width
        self.update_vertices()
        self.rotation += self.rotation_speed
	
    def is_alive(self):
        return (self.ttl > 0)

class Source(GuiGroup):
    def __init__(self,x,y,max,atlas):
        GuiGroup.__init__(self,[],x,y,0,0)
        self.max = max
        self.atlas = atlas
	
    def update(self):
        GuiGroup.update(self)
        # Spawn a new particle, we we have space
        if len(self.objectList) < self.max:
			self.objectList.append(self.spawn())
		
        # Check for dead particles, and clean 'em eup
        dead_particles = []
        for particle in self.objectList:
            particle.update()
            if particle.is_alive() == False:
                dead_particles.append(particle)
        for dead_particle in dead_particles:
            self.objectList.remove(dead_particle)
        
    def draw(self):
        for particle in self.objectList:
            particle.draw()
            particle.undraw()
	
    def spawn(self):
        velocity = [(random.random()-0.5)*5,(random.random()-0.5)*5]
        return Particle(self.x,self.y,velocity,random.randint(75,150),self.atlas)
    
    def empty(self):
        return len(self.objectList) == 0

class DeathSource(Source):
    def __init__(self,x,y,atlas):
        Source.__init__(self,x,y,20,atlas)
        self.filled = False
    
    def spawn(self):
        velocity = [(random.random()-0.5)*5,(random.random()-0.5)*5]
        return DeathParticle(self.x,self.y,velocity,random.randint(50,75),self.atlas)
	
    def update(self):
        GuiGroup.update(self)
        # Spawn a new particle, we we have space
        if len(self.objectList) < self.max:
            if not self.filled:
                self.objectList.append(self.spawn())
                self.objectList.append(self.spawn())
        else:
		    self.filled = True
		
        # Check for dead particles, and clean 'em eup
        dead_particles = []
        for particle in self.objectList:
            particle.update()
            if particle.is_alive() == False:
                dead_particles.append(particle)
        for dead_particle in dead_particles:
            self.objectList.remove(dead_particle)

class DeathParticle(Particle):
    def __init__(self,x,y,velocity,ttl,atlas):
        keys = ["blood1","blood2","blood3","blood4","blood5","bone","skull","rib","rib2"]
        Particle.__init__(self,x,y,velocity,ttl,atlas,keys[random.randint(0,len(keys)-1)])
        self.rotation_speed = random.randint(-30,30)
        if self.key.find("blood") > -1:
            self.color = [1.0,0.75,0.5,1.0]
        else:
            self.color = [1.0,1.0,1.0,1.0]
import OpenGL
from OpenGL.GL import *
from OpenGL import constants, error
from OpenGL.GLU import *
from OpenGL.arrays import arraydatatype

class GuiObject:
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.color = [1.0, 1.0, 1.0, 1.0]
        self.width = width
        self.height = height
        self.rotation = 0
        
        self.update_vertices()
    
    def update_vertices(self):
        self.vertices = [
            [-self.width/2,-self.height/2,-1],
            [self.width/2,-self.height/2,-1],
            [-self.width/2,self.height/2,-1],
            [self.width/2,self.height/2,-1]
        ]
    
    def draw(self):        
        glTranslate(self.x,self.y,0.0)
        glRotate(self.rotation,0,0,1.0)
    
    def undraw(self):        
        glRotate(-self.rotation,0,0,1.0)
        glTranslate(-self.x,-self.y,0.0)
    
    def update(self):
        pass
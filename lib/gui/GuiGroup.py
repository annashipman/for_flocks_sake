import OpenGL
from OpenGL.GL import *
from OpenGL import constants, error
from OpenGL.GLU import *
from OpenGL.arrays import arraydatatype
from GuiObject import GuiObject

class GuiGroup(GuiObject):
    def __init__(self, objectList, x,y,width,height):
        GuiObject.__init__(self, x, y, width, height)
        self.objectList = objectList    
    
    def draw(self): 
        GuiObject.draw(self)   
        for guiObject in self.objectList:
            guiObject.draw()
            guiObject.undraw()    
    
    def set_color(self,color):
        for o in self.objectList:
            o.color = color
        
    def update(self):
        GuiObject.update(self)   
        for guiObject in self.objectList:
            guiObject.update()

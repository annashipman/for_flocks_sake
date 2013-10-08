import OpenGL
from OpenGL.GL import *
from OpenGL import constants, error
from OpenGL.GLU import *
from OpenGL.arrays import arraydatatype
from GuiObject import GuiObject

class GuiColorRect(GuiObject):
    def __init__(self,x,y,width,height):
        GuiObject.__init__(self,x,y,width,height)
    
    def draw(self):    
        GuiObject.draw(self)
        
        glDisableClientState(GL_NORMAL_ARRAY)
        glDisableClientState(GL_TEXTURE_COORD_ARRAY)
        glBindTexture(GL_TEXTURE_2D, 0)
        glColor4f(self.color[0],self.color[1],self.color[2],self.color[3])
        glVertexPointer(3, GL_FLOAT, 0, self.vertices)
        glDrawArrays(GL_TRIANGLE_STRIP, 0, 4)
    
    def undraw(self):
        GuiObject.undraw(self)
        
        glEnableClientState(GL_NORMAL_ARRAY)
        glEnableClientState(GL_TEXTURE_COORD_ARRAY)
    
    def update(self):
        pass
import pygame
import OpenGL 
OpenGL.CONTEXT_CHECKING = True
OpenGL.FORWARD_COMPATIBLE_ONLY = True
from OpenGL.GL import *
from OpenGL import constants, error
from OpenGL.GLU import *
from OpenGL.arrays import arraydatatype
from OpenGL.extensions import alternate
import ctypes
from OpenGL.GL.framebufferobjects import *
from OpenGL.GL.EXT.multi_draw_arrays import *
from OpenGL.GL.ARB.imaging import *

class AbstractScreen:
    # Create a new AbstractScreen. Don't do this, obviously.
    def __init__(self):
        self.previous = None
        self.renderables = []
    
    def on_focus(self):
        pass
    
    def update(self):
        for guiObject in self.renderables:
            guiObject.update()
        return True
    
    def draw(self):        
        glClearColor(0.5, 0.5, 0.5, 0.01)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glLoadIdentity()
        for renderable in self.renderables:
            renderable.draw()
            renderable.undraw()

        pygame.display.flip()
    
    def add(self,item):
        self.renderables.append(item)
    
    def remove(self,item):
        self.renderables.remove(item)
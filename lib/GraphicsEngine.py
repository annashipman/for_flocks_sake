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

import pygame
from GuiTextureInfo import GuiTextureInfo
from State import State

class GraphicsEngine:
    __shared_state = {}
    # options is a dictionary with the following keys:
    #     width
    #     height
    def __init__(self):
        self.__dict__ = self.__shared_state
    
    def setup(self):
        self.textures = []
        
        # Get a pygame context into which we can render
        pygame.display.init()
        display_options = pygame.HWSURFACE | pygame.OPENGL | pygame.DOUBLEBUF
        if State().fullscreen:
            display_options = display_options | pygame.FULLSCREEN
        self.screen = pygame.display.set_mode( State().screen_size, display_options )
        
        # Set up an OpenGL viewport for 2d rendering
        glMatrixMode(GL_PROJECTION)
        glOrtho(0.0, State().screen_size[0], 0.0, State().screen_size[1], 0.01, 20.00)
        glViewport(0, 0, State().screen_size[0], State().screen_size[1])
        glMatrixMode(GL_MODELVIEW)
        glDisable(GL_DEPTH_TEST)
        glEnable(GL_TEXTURE_2D)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glEnableClientState(GL_VERTEX_ARRAY)
        glEnableClientState(GL_NORMAL_ARRAY)
        glEnableClientState(GL_TEXTURE_COORD_ARRAY)
        glLoadIdentity()
    
    def draw(self,screen):
        screen.draw()
    
    def load_image(self,image):
        # Check to see if we've already loaded this file into a texture
        for info in self.textures:
            if info.filename == image:
                return info
        
        # Load the image with pygame, do some magic (tostring!?), and save it in the texture list
        textureSurface = pygame.image.load(image).convert_alpha()
        textureData = pygame.image.tostring(textureSurface, "RGBA", 1)

        width = textureSurface.get_width()
        height = textureSurface.get_height()

        texture = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, texture)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, textureData)

        textureInfo = GuiTextureInfo(image,width,height,texture)
        self.textures.append(textureInfo)
        return textureInfo
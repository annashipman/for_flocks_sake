import OpenGL
from OpenGL.GL import *
from OpenGL import constants, error
from OpenGL.GLU import *
from OpenGL.arrays import arraydatatype
from GuiObject import GuiObject
from GraphicsEngine import GraphicsEngine

class GuiSprite(GuiObject):
    def __init__(self,x,y,surface,texture_key=None):
        GuiObject.__init__(self,x,y,0,0)
        self.surface = surface
        graphics_engine = GraphicsEngine()
        if texture_key == None:
            self.texture_info = graphics_engine.load_image(surface)
        else:
            self.texture_info = graphics_engine.load_image(surface.name + ".png")
        
        # Normals
        self.normals = []
        for i in range(0,3):
            self.normals.append([0,0,0])
            
        # Vertices and texture coords
        if texture_key == None:
            self.width = self.texture_info.width
            self.height = self.texture_info.height
            self.update_vertices()
            
            self.texture_coords = [
                [0.0,1.0],
                [1.0,1.0],
                [0.0,0.0],
                [1.0,0.0]
            ]
        else:
            texture = self.surface.texture(texture_key)
            self.width = texture.width
            self.height = texture.height
            self.render_from_atlas(texture_key)
    
    def render_from_atlas(self,texture_key):
        texture = self.surface.texture(texture_key)
        self.update_vertices()

        self.texture_coords = [
            [float(texture.x) / self.texture_info.width,(float(texture.y) + texture.height) / self.texture_info.height],
            [(float(texture.x) + texture.width) / self.texture_info.width,(float(texture.y) + texture.height) / self.texture_info.height],
            [float(texture.x) / self.texture_info.width,float(texture.y) / self.texture_info.height],
            [(float(texture.x) + texture.width) / self.texture_info.width, float(texture.y) / self.texture_info.height]
        ]
    
    def draw(self):    
        GuiObject.draw(self)
        
        glColor4f(self.color[0],self.color[1],self.color[2],self.color[3])
        glBindTexture(GL_TEXTURE_2D,self.texture_info.texture_id);
        glVertexPointer(3, GL_FLOAT, 0, self.vertices);
        glNormalPointer(GL_FLOAT,0,self.normals);
        glTexCoordPointer(2,GL_FLOAT,0,self.texture_coords);
        glDrawArrays(GL_TRIANGLE_STRIP, 0, 4);
        
    def undraw(self):
        GuiObject.undraw(self)
    
    def update(self):
        pass

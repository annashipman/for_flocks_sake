from GuiAtlas import GuiAtlas
from GuiGroup import GuiGroup
from GuiSprite import GuiSprite
import random

class GuiString(GuiGroup):
    def __init__(self,x,y,string,atlas,scale=1.0,easter=False):
        self.font = atlas
        self.easter = easter
        GuiGroup.__init__(self,[],x,y,0,0)
        self.scale = scale
        self.set_string(string)
        self.alpha = 1.0
    
    def set_alpha(self,alpha):
        if alpha > 1.0:
            alpha = 1.0
            
        for o in self.objectList:
            o.color[3] = alpha
        self.alpha = alpha
    
    def get_alpha(self):    
        return self.alpha
    
    def set_string(self,string):
        self.objectList = []
        self.width = 0
        self.height = 0
        for i in range(0,len(string)):
            try:
                char = GuiSprite(self.width,0,self.font,string[i]+"")
                if self.easter:
                    char.color = [random.random()/3.0+0.7,random.random()/3.0+0.7,random.random()/3.0+0.7,1.0]
                char.width *= self.scale
                char.height *= self.scale
                char.update_vertices()
                self.objectList.append(char)
                self.width += char.width
                if self.height < char.height:
                    self.height = char.height
            except:
                self.width += 32*self.scale
        for x in self.objectList:
            x.x -= self.width/2
    
    def alive(self):
        return True
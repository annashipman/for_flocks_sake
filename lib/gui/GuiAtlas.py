from GraphicsEngine import GraphicsEngine

class GuiTextureCoords:
    def __init__(self,x,y,w,h):
        self.x = x
        self.y = y
        self.width = w
        self.height = h

class GuiAtlas:
    def __init__(self,name):
        self.name = name
        graphics = GraphicsEngine()
        texture_info = graphics.load_image(name+".png")
        
        self.textures = {}
        atlas_file = open(name+".atlas",'r')
        for line in atlas_file:
            col = line.split("\t")
            texture = GuiTextureCoords(int(col[1]),texture_info.height-int(col[2])-int(col[4]),int(col[3]),int(col[4]))
            self.textures[col[0]] = texture
        atlas_file.close()
    
    def texture(self,key):
        return self.textures[key]

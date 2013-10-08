from GraphicsEngine import GraphicsEngine
from GuiSprite import GuiSprite
from State import State

class GuiLevel:
    def __init__(self,name, atlas):
        self.name = name
        self.width = 256
        self.height = 256

        self.tiles = {}
        level_file = open(name+".level",'r')
        for line in level_file:
            col = line.split(",") 
            tileX = int(col[0])
            tileY = int(col[1])
            tileRef = col[2].rstrip()
            tile = GuiSprite(tileX, tileY, atlas, tileRef)
            self.tiles[(int(col[0]), int(col[1]))] = tile                        
            tile.rotation = 180
        level_file.close()
        self.hellifying = False

    def drawAltBackground(self,ax,ay):
        tile_width = 256
        tile_height = 256
        x = State().player.x-State().player.x%tile_width
        y = State().player.y-State().player.y%tile_height
        
        center = self.tiles[(x,y)]
        for xi in range(-2,3):
            for yi in range(-2,3):
                try:
                    a_tile = (x+xi*tile_width,y+yi*tile_height)
                    if a_tile[0] >= 0 and a_tile[1] >= 0:
                        self.tiles[a_tile].draw()
                        self.tiles[a_tile].undraw()
                except:
                    pass
                    
    def hellify(self):
        self.hellifying = True
    
    def update(self):
        if self.hellifying:
            for pair in self.tiles.items():
                gb = pair[1].color[1]
                if gb > 0.2:
                    gb -= 0.05
                    pair[1].color = [1.0,gb,gb,1.0]
                    State().point.color = pair[1].color

    def drawBackground(self,x,y):
        self.xOffset = State().screen_size[0]/2
        self.yOffset = State().screen_size[1]/2                      
        
        for tile in self.tiles.items():
            tileX = tile[0][0]
            tileY = tile[0][1]
            
            if ((x > tileX) and (x <= tileX + self.width)) and ((y > tileY) and (y <= tileY + self.height)):
                #draw the tile 
                tile[1].x = self.xOffset
                tile[1].y = self.yOffset

                tile[1].draw()
                tile[1].undraw()
                
                #draw the tile above
                try:
                    northX = tileX                    
                    northY = tileY + self.height

                    currentTile = self.tiles[(northX,northY)]

                    currentTile.x = self.xOffset
                    currentTile.y = self.yOffset + self.height    
                
                    currentTile.draw()
                    currentTile.undraw()
                except KeyError:
                    print "no tile at : " + str(northX) + " " + str(northY)
  
                #and the one below            
                try:                
                    southX = tileX  
                    southY = tileY - self.height
                
                    currentTile = self.tiles[(southX,southY)]
                
                    currentTile.x = self.xOffset    
                    currentTile.y = self.yOffset - self.height    
                
                    currentTile.draw()
                    currentTile.undraw()   
                except KeyError:
                     print "no tile at : " + str(southX) + " " + str(southY)

                #and now draw the column to the right
                newColumnX = northX + self.width
                newColumnY = northY
                actualX = self.xOffset + self.width  
                
                self.drawColumn(newColumnX,newColumnY, actualX)
                
                #one to the left
                newColumnX = northX - self.width
                actualX = self.xOffset - self.width
                self.drawColumn(newColumnX,newColumnY,actualX) 

    def drawColumn(self,topX,topY,actualX):
        #top one
        try:         
            newColumnTile = self.tiles[(topX,topY)]
            newColumnTile.x = actualX   
            newColumnTile.y = self.yOffset + self.height
                
            newColumnTile.draw()
            newColumnTile.undraw()

        except KeyError:
            print "no tile at : " + str(topX) + " " + str(topY)   

        #level with player
        try:
            nextTileX = topX
            nextTileY = topY - self.height

            newColumnTile = self.tiles[(nextTileX,nextTileY)]    

            newColumnTile.x = actualX   
            newColumnTile.y = self.yOffset

            newColumnTile.draw()
            newColumnTile.undraw()

        except KeyError:
            print "no tile at : " + str(nextTileX) + " " + str(nextTileY)   
 
        #bottom
        try:
            nextTileX = topX
            nextTileY = nextTileY - self.height

            newColumnTile = self.tiles[(nextTileX,nextTileY)]    

            newColumnTile.x = actualX   
            newColumnTile.y = self.yOffset - self.height

            newColumnTile.draw()
            newColumnTile.undraw()

        except KeyError:
            print "no tile at : " + str(nextTileX) + " " + str(nextTileY)   
        

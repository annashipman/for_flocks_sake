from GuiSprite import GuiSprite

class GuiAnimation(GuiSprite):
    def __init__(self,x,y,atlas,keys,start_frame=0,play_once=False):
        GuiSprite.__init__(self,x,y,atlas,keys[start_frame])
        self.keys = keys
        self.frame = start_frame
        self.play_once = play_once
        self.dead = False
    
    def update(self):
        if not self.dead:
            self.frame += 1
            if self.frame >= len(self.keys):
                if self.play_once:
                    self.dead = True
                    self.frame = 0
                else:
                    self.frame = 0
            self.render_from_atlas(self.keys[self.frame])
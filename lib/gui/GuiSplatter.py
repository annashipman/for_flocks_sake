from GuiAnimation import GuiAnimation

class GuiSplatter(GuiAnimation):
    def __init__(self,x,y,atlas,keys):
        GuiAnimation.__init__(self,x,y,atlas,keys,0)
        self.keys = keys
        self.frame = 0
        self.play_once = True
        self.dead = False
        self.dying = False
    
    def update(self):
        if self.dying:
            self.color[3] -= 0.5
            if self.color[3] <= 0.0:
                self.dead = True
        else:
            self.frame += 1
            if self.frame >= len(self.keys):
                if self.play_once:
                    self.dying = True
                    self.frame = 0
                else:
                    self.frame = len(self.keys)-1
            self.render_from_atlas(self.keys[self.frame])
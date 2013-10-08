import os
import config
import math

def import_libs(dir):
        library_list = {} 
    
        for f in os.listdir(os.path.abspath(dir)):
            module_name, ext = os.path.splitext(f) # Handles no-extension files, etc.
            if ext == '.py': # Important, ignore .pyc/other files.
                print 'imported module: %s' % (module_name)
                module = __import__(module_name)
                library_list[module_name] = module
        return library_list

class State:
    __shared_state = {}
    
    def __init__(self):
        self.__dict__ = self.__shared_state
        
    def init_state(self):
        self.debug = config.Debug
        self.screen_size = config.ScreenSize
        self.fullscreen = config.Fullscreen
        self.framerate = config.Framerate
        self.game_size = config.GameSize
        self.diagonal = math.sqrt(pow(self.screen_size[0],2)+pow(self.screen_size[1],2))
        self.audio = config.Audio
        self.fire_count = config.FireCount
        self.max_time = config.MaxTime
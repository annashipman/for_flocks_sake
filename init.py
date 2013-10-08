import sys
sys.path += ['.']
from ctypes import util
try:
    from OpenGL.platform import win32
except AttributeError:
    pass
import os
import pygame
import random

from pygame.locals import *
from game import *
from State import State

try:
    import psyco
except:
    print "psyco not available"

def main():
    state = State()
    state.init_state()
    state.framerate = 30
    alive = True
    clock = pygame.time.Clock()
    app = game(clock)
    index = 0
    # Initialize joystick
    
    pygame.init()
    State().gamepad = None
    xboxpad = pygame.joystick.get_count()
    if xboxpad > 0:
        State().gamepad = pygame.joystick.Joystick(0)
        State().gamepad.init()
            
    while alive:
        # Events
        if pygame.event.peek(QUIT):
            alive = False
        events = pygame.event.get()
        
        # Pump events to game
        for event in events:
            app.handle_event(event)
        
        # Update state
        update = app.update()
        # Draw
        app.draw()
        
        # Are we done?
        alive = app.alive
        
        # Did we update anything?
        if update:
            # if so, redraw screen
            pass
        
        # Regular framerate
        clock.tick(state.framerate)
        
        # Print fps regularly
        if State().debug:
            index += 1
            if index > 30:
                index = 0
                print clock.get_fps()," FPS"

if __name__ == '__main__':
    try:
        psyco.full()
    except:
        pass
    main()


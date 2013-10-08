from GenericBoid import GenericBoid
from State import State
from Calculations import Calculations
from math import cos,radians,sin
from BoidSteering import BoidSteering

# Predator class for birds level. Hawks have two modes, active and passive;
# switch between the two as in:
#
#     a_hawk = Hawk(0,0,texture_atlas)
#     ...
#     a_hawk.active() # Make active, changing the speed (to fast) and the animation
#     a_hawk.passive() # Make passive
#
# Hawks start out in passive mode.

class Hawk(GenericBoid):
    def __init__(self,x,y,atlas,start_frame=0):
        self.passive_frames = ["hawk01."+str(i) for i in range(1,9)]
        self.active_frames = ["hawk01.10"]
        
        GenericBoid.__init__(self,x,y,atlas,self.passive_frames,start_frame)
        self.passive()
        self.goal_speed = self.speed
        self.position = (x,y)
        self.steering = BoidSteering()
        self.isActive = False
        
    def active(self):
        self.set_active(True)
    
    def draw(self):
        self.rotation -= 90
        GenericBoid.draw(self)
    
    def passive(self):
        self.set_active(False)
        self.isActive = False
    
    def set_active(self,bool):
        if bool:
            self._set_frames(self.active_frames)
            self.goal_speed = State().boid_speed * 2
        else:
            self._set_frames(self.passive_frames)
            self.goal_speed = State().boid_speed / 2.0

        self.isActive = True
    
    def _set_frames(self,frameset):
        self.keys = frameset

    def getPosition(self):
        return GenericBoid.getPosition(self)
    

    def getFuturePositions(self, boid):
        speed = boid.speed
        angle = boid.orientation
        futurePosX = boid.x
        futurePosY = boid.y

        xVelocity = cos(radians(angle-90)) * speed
        yVelocity = sin(radians(angle-90)) * speed
        futurePosX += (xVelocity * 8)
        futurePosY += (yVelocity * 8)
        
        return (futurePosX, futurePosY)


    def update(self):
        GenericBoid.update(self)
        playerHawkDistance = Calculations().getDistance(State().player.getPosition(), GenericBoid.getPosition(self))

        if playerHawkDistance < 800 and self.isActive == False:
            playerFuturePosition = self.getFuturePositions(State().player)
            angle = Calculations().getAngle(GenericBoid.getPosition(self), playerFuturePosition)
            GenericBoid.setOrientation(self, angle)
            self.active()
        elif playerHawkDistance > 800:
            self.passive()

        if self.speed != self.goal_speed:
            if self.speed < self.goal_speed:
                self.speed += 6.0
                if self.speed > self.goal_speed:
                    self.speed = self.goal_speed
            else:
                self.speed -= 6.0
                if self.speed < self.goal_speed:
                    self.speed = self.goal_speed

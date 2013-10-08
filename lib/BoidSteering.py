from Calculations import Calculations

class BoidSteering:
    def __init__(self):
        self.angle = 0#
        self.relativeAngle = 0
    
    #This steers the boid to a location
    def steerBoids(self,boid,averagePos):
        self.relativeAngle = 0
        #get the angle between the 2 points
        self.angle = Calculations().getAngle(boid.getPosition(),averagePos)
        
        #get the relative angle of the angle where the boid is facing
        self.relativeAngle = self.angle - boid.orientation
        
        #If the relative angle is less than 0 then fix it so its not
        if self.relativeAngle < 0:
            self.relativeAngle += 360 
        elif self.relativeAngle > 360:
            self.relativeAngle -= 360       
        
        #If the target is to the right of the boid then turn right
        if self.relativeAngle > 5 and self.relativeAngle <= 180:
            boid.orientation += 9

            #If the target is to the left of the boid then turn left        
        elif self.relativeAngle > 180 and self.relativeAngle < 355:
            boid.orientation -= 9
         
        #The boids orientation is greater than 359 or is less than 0 fix it
        if boid.orientation > 359:
            boid.orientation -= 360
        elif boid.orientation < 0:
            boid.orientation += 360

    #This steers the boid to a location
    def huntBoids(self,boid,averagePos):
        self.relativeAngle = 0
        #get the angle between the 2 points
        self.angle = Calculations().getAngle(boid.getPosition(),averagePos)

        #get the relative angle of the angle where the boid is facing
        self.relativeAngle = self.angle - boid.orientation

        #If the relative angle is less than 0 then fix it so its not
        if self.relativeAngle < 0:
            self.relativeAngle += 360
        elif self.relativeAngle > 360:
            self.relativeAngle -= 360

        #If the target is to the right of the boid then turn right
        if self.relativeAngle > 15 and self.relativeAngle <= 180:
            boid.orientation += 25

            #If the target is to the left of the boid then turn left
        elif self.relativeAngle > 180 and self.relativeAngle < 345:
            boid.orientation -= 25

        #The boids orientation is greater than 359 or is less than 0 fix it
        if boid.orientation > 359:
            boid.orientation -= 360
        elif boid.orientation < 0:
            boid.orientation += 360
            
    def avoidBoids(self,boid,decision):
        if decision == "right":
            boid.orientation += 6
        elif decision == "left":
            boid.orientation -= 6

            
    

from BoidSteering import BoidSteering
from Calculations import Calculations
from math import cos,radians,sin
from State import State
import time
from scoreTracker import Score
import random
from GuiAlert import GuiAlert

class SwarmBot:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.averagePos = 0,0
        self.steering = BoidSteering()
        self.boidCal = Calculations()
        self.flockCount = 0
        self.frameCount = 0
        self.frameSkip = 1
        self.first_drop_timer = 0
        self.drop_count = 0

    def updateBoids(self, maxMapSize, boids, playerBoid, holdingPoint):
        if self.frameCount == 0:
            dead_birds = []
            holdingPenRadius = 100
            flockingDistance = 150 + self.flockCount * 23
            State().flock = []
            all_inc_player = [x for x in boids]
            all_inc_player.append(playerBoid)
            self.flockCount = 0
            for boid in boids:
                if boid.boidState == "Dead":
                    dead_birds.append(boid)
                if not boid.isCaptured:
                    for fire in State().fires:
                        if self.boidCal.distance(fire,boid) < 45 and boid.kill():
                            fire_death_alert = GuiAlert(boid.x,boid.y,"bird lost",State().font,0.5)
                            State().map_alerts.append(fire_death_alert)
                            fire_death_alert.set_color([1.0,0.5,0.25,1.0])
                    if not self.checkIfGoingOffScreen(boid, maxMapSize):
                        collision = self.checkForCollisions(all_inc_player, boid)
                        #If the boid is not going to collide then mover towards the average boid position
                        if collision == False:
                            playerDistance = self.boidCal.getDistance(boid.getPosition(), playerBoid.getPosition())
                            if playerDistance <= flockingDistance and playerBoid.boidState == "Normal":
                                self.isInFlock = True
                                self.flockCount += 1
                                self.steering.steerBoids(boid, playerBoid.getPosition())
                                State().flock.append(boid)
                                boid.speed = State().player.speed
                                boid.color = [0.5,1,0.5,1]
                                holdingPointDistance = self.boidCal.getDistance(boid.getPosition(), holdingPoint.getPosition())
                                if holdingPointDistance <= holdingPenRadius:
                                    boid.isCaptured = True
                                    boid.color = [1,1,1,1]
                                    boid.alternate_frames()
                                    now = time.time()
                                    if now - self.first_drop_timer > 2.0:
                                        self.first_drop_timer = now
                                        self.drop_count = 0
                                    self.drop_count += 1
                                    Score().scoreUpdateDrop(self.drop_count)
                                    State().map_alerts.append( GuiAlert(boid.x,boid.y,str(self.drop_count)+"x",State().font,0.5))
                            else:
                                self.isInFlock = False
                                boid.rotation_speed = 0
                                boid.speed = State().boid_speed
                                boid.color = [1,1,1,1]
                    # else: # Captured
                    #     angle = self.boidCal.getAngle(boid.getPosition(), holdingPoint.getPosition())
                    #     boid.orientation -= (angle - boid.orientation)/10.0

                else:
                    holdingPointDistance = self.boidCal.getDistance(boid.getPosition(), holdingPoint.getPosition())
                    if holdingPointDistance > holdingPenRadius - 20:
                        #self.steering.avoidBoids(boid, "right")
                        boid.orientation += 9        
            for dead_bird in dead_birds:
                State().boids.remove(dead_bird)
        self.flockCount = len(State().flock)
        self.frameCount += 1

        if self.frameCount > self.frameSkip:
            self.frameCount = 0
        return self.averagePos

    def avoidHawk(self, hawk, boids):
        for boid in boids:
            if boid.isCaptured == False:
                hawkDistance = self.boidCal.getDistance(hawk.getPosition(), boid.getPosition())
                if hawkDistance < 300:
                    self.avoid(boid, hawk)

    def checkToAvoidTrees(self, treePositionList, boids):
        for boid in boids:
            if boid.isCaptured == False:
                for treePosition in treePositionList:
                    futureBoidPosition = self.getFuturePositions(boid)
                    treeDistance = self.boidCal.getDistance(futureBoidPosition, treePosition)
                    if treeDistance < 128:
                        self.avoidTree(boid, treePosition)

    def checkIfGoingOffScreen(self, boid, maxMapSize):
        futurePosition = self.getFuturePositions(boid)
        direction = None

        #Check to see if the boids move either past the min xPosition or past the max xPosition
        if futurePosition[0] <= 0 or futurePosition[0] >= maxMapSize[0] or futurePosition[1] <= 0 or futurePosition[1] >= maxMapSize[1]:
            direction = "left"
            boid.hit_wall_ttl = 1
        elif boid.hit_wall_ttl > 0:
            boid.hit_wall_ttl -= 1
            direction = "left"

        if direction != None and not boid.return_to_world:
            boid.return_to_world = True
            boid.rotation_speed = 0
            boid.speed = State().boid_speed
#            self.steering.avoidBoids(boid, direction)
            boid.orientation -= 180
        else:
            if  boid.return_to_world:
                boid.rotation_speed = 0
            boid.return_to_world = False

        return direction

    def getFuturePositions(self, boid):
        speed = boid.speed
        angle = boid.orientation
        futurePosX = boid.x
        futurePosY = boid.y

        xVelocity = cos(radians(angle-90)) * speed
        yVelocity = sin(radians(angle-90)) * speed
        futurePosX += (xVelocity * 3)
        futurePosY += (yVelocity * 3)

        return (futurePosX,futurePosY)

    def checkForCollisions(self, boids, boid):
        closestObjectdistance = 100000; # This is the distance of the nearest boid
        collision = False
        minDistance = 60

        #Get future posistion of the boid
        boid1FuturePos = self.getFuturePositions(boid)

        for currentBoid in boids:
            if currentBoid != boid and currentBoid.isCaptured != True:
                if boid.isInFlock == True and currentBoid.isInFlock == True or boid.isInFlock == False and currentBoid.isInFlock == False:
                    xPositionDifference = currentBoid.getPosition()[0] - boid.getPosition()[0]
                    yPositionDifference = currentBoid.getPosition()[1] - boid.getPosition()[1]
                    if xPositionDifference > -300 and xPositionDifference < 300 and yPositionDifference > -300 and yPositionDifference < 300:
                        #Get the future positions of the other boid
                        boid2FuturePos = self.getFuturePositions(currentBoid)
                        distance = self.boidCal.getDistance(boid1FuturePos, boid2FuturePos)
                        if distance <= minDistance and distance < closestObjectdistance:
                            closestObjectdistance = distance
                            collision = True
                            boid2 = currentBoid

        if collision == True:
            self.avoid(boid, boid2)

        return collision

    def avoid(self, boid1, boid2):
        relativeAngle = 0
        #get the angle between the two boids
        angle = self.boidCal.getAngle(boid1.getPosition(),boid2.getPosition())
        direction = ""
        #find the relative angle of the boid 2 is from boid1
        relativeAngle = angle - boid1.orientation

        if relativeAngle < 0:
            relativeAngle += 360

        #If sprite one is more to the right than sprite two then turn left
        if relativeAngle >= 0  and relativeAngle <= 180:
            direction = "left"
        #If sprite one is more to the left than sprite two then turn right
        elif relativeAngle > 180 and relativeAngle < 360:
            direction = "right"

        self.steering.avoidBoids(boid1, direction)


    def avoidTree(self, boid1, treePosition):
        relativeAngle = 0
        #get the angle between the two boids
        angle = self.boidCal.getAngle(boid1.getPosition(), treePosition)
        direction = ""
        #find the relative angle of the boid 2 is from boid1
        relativeAngle = angle - boid1.orientation

        if relativeAngle < 0:
            relativeAngle += 360

        #If sprite one is more to the right than sprite two then turn left
        if relativeAngle >= 0  and relativeAngle <= 180:
            direction = "left"
        #If sprite one is more to the left than sprite two then turn right
        elif relativeAngle > 180 and relativeAngle < 360:
            direction = "right"

        self.steering.avoidBoids(boid1, direction)

#This update function updates the sprites position on screen  
    def calculateAveragePos(self,boids):
        self.x = 0
        self.y = 0
        self.averagePos = 0,0
        self.count = 0

        for sprite in boids:
            x,y = sprite.getCenterPosition()
            self.x += x
            self.y += y
            self.count += 1

        self.averagePos = (self.x/self.count),(self.y/ self.count)

    def getAveragePos(self):
        return self.averagePos

    def moveToHoldingArea(self, playerBoid, holdingPoint):
        playerDistance = self.boidCal.getDistance(playerBoid.getPosition(), holdingPoint.getPosition())
        if playerDistance > 120:
            self.steering.steerBoids(playerBoid, holdingPoint.getPosition())
        else:
            if playerBoid.current == "deathEater":
                playerBoid.speed = 18
                playerBoid.boidState = "Genocide!"
            elif playerBoid.current == "norm":
                State().player.convert("conversion")

    def slaughterTheFlockers(self, playerBoid, boids):
        targetBoids = []
        boidsSlaughtered = False

        for boid in boids:
            if boid.isCaptured == True and boid.boidState != "Dead":
                targetBoids.append(boid)

        if len(targetBoids) > 0:
            targetPosition = (0, 0)
            count = 0
            minDistance = 0
            for boid in targetBoids:
                playerDistance = self.boidCal.getDistance(playerBoid.getPosition(), boid.getPosition())
                if playerDistance < 20 and not boid.dying:
                    boid.kill()
                    reward = ["tasty","crunchy","delicious","salty","tender","bacon flavoured","tastes like chicken","edible"]
                    death_alert = GuiAlert(boid.x,boid.y,reward[random.randint(0,len(reward)-1)],State().font,0.5)
                    Score().scoreUpdateDrop(2)
                    State().map_alerts.append(death_alert)
                    death_alert.set_color([1.0,0.5,0.25,0.0])
                    
                if count == 0:
                    minDistance = playerDistance
                    targetPosition = boid.getPosition()
                else:
                    if playerDistance < minDistance:
                        minDistance = playerDistance
                        targetPosition = boid.getPosition()
            self.steering.huntBoids(playerBoid, targetPosition)
        else:
            boidsSlaughtered = True


        return boidsSlaughtered




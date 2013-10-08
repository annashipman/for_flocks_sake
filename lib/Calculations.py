import os
import math

class Calculations:
	def getAngle(self,sprite1Pos,sprite2Pos):

		distance = 0.0
		b = 0.0
		c = 0.0
		objectOrientation = 0

		#This calculates the distance between the the two sprites
		x1,y1 = sprite1Pos   
		x2,y2 = sprite2Pos

		#If sprite one is more to the right than sprite two then b equals sprite 1 - sprite 2
		if x1 > x2:
			b = x1 - x2
		#If sprite two is more to the right than sprite one then b equals sprite 1 - sprite 2   
		elif x2 > x1:
			b = x2 - x1

		#If sprite on is below sprite two then c equals sprite 1 - sprite 2
		if y1 > y2:
			c = y1 - y2
		#If sprite one is above sprite two then c equals sprite 1 - sprite 2
		elif y2 > y1:
			c = y2 - y1

		#Calculates the distance between the 2 objects
		distance = pow(b,2) + pow(c,2)
		distance = math.sqrt(distance)
		if distance != 0:
			objectOrientation = (math.asin(c/distance)) * (180/3.141592920354)
                
		#If the first object is above the second object
		if x1 == x2 and y1 < y2:
			objectOrientation = 180

		#If the first object is below the second object
		elif x1 == x2 and y1 > y2:
			objectOrientation = 0

		#If the player is to the left of the object
		elif x1 < x2 and y1 == y2:
			objectOrientation = 90
        
		#If the player is to the right of the object
		elif x1 > x2 and y1 == y2:
			objectOrientation = 270

		#If the player is to the right and above the object
		elif x1 > x2 and y1 < y2:
                    objectOrientation = 270 - objectOrientation

		#If the player is to the left and above the object
		elif x1 < x2 and y1 < y2:
                    objectOrientation = objectOrientation + 90
        
		#If the player is to the right and below the object
		elif x1 > x2 and y1 > y2:
                    objectOrientation = objectOrientation + 270

		#If the player is to the left and below the object
		elif x1 < x2 and y1 > y2:
                    objectOrientation = 90 - objectOrientation
               
		return objectOrientation
	
	def distance(self,a,b):
	    return math.sqrt(pow(b.x-a.x,2)+pow(b.y-a.y,2))
	
	def getDistance(self,spritePos1,spritePos2):
		
		distance = 0.0
		b = 0.0
		c = 0.0
		#This calculates the distance between the the two sprites
		x1,y1 = spritePos1	
		x2,y2 = spritePos2

		#If sprite one is more to the right than sprite two then b equals sprite 1 - sprite 2
		if x1 > x2:
			b = x1 - x2
		#If sprite two is more to the right than sprite one then b equals sprite 1 - sprite 2	
		elif x2 > x1:
			b = x2 - x1

		#If sprite one is below sprite two then c equals sprite 1 - sprite 2
		if y1 > y2:
			c = y1 - y2
		#If sprite one is above sprite two then c equals sprite 1 - sprite 2
		elif y2 > y1:
			c = y2 - y1

    	#Calculates the distance between the 2 objects
		distance = pow(b,2) + pow(c,2)
		distance = math.sqrt(distance)
		
		return distance

	def getXDistance(self,spritePos1,spritePos2):
		
		xDistance = 0.0
		x1,y1 = spritePos1
		x2,y2 = spritePos2
		
		#If sprite one is more to the right than sprite two then xDistance equals sprite 1 - sprite 2
		if x1 > x2:
			xDistance = x1 - x2
		#If sprite two is more to the right than sprite one then xDistance equals sprite 1 - sprite 2	
		elif x2 > x1:
			xDistance = x2 - x1
			
		return xDistance
		
	def getYDistance(self,spritePos1,spritePos2):
		yDistance = 0.0
		x1,y1 = spritePos1
		x2,y2 = spritePos2
		
		#If sprite one is more to the right than sprite two then yDistance equals sprite 1 - sprite 2
		if y1 > y2:
			yDistance = y1 - y2
		#If sprite two is more to the right than sprite one then yDistance equals sprite 1 - sprite 2	
		elif y2 > y1:
			yDistance = y2 - y1
			
		return yDistance
				 		
		 		
	def getRelativeAngle(self,angle,orientation):

		relativeAngle = 0.0

		#find the relative angle
		relativeAngle = angle - orientation
        
		if relativeAngle < 0:
			relativeAngle += 360
            
		return relativeAngle

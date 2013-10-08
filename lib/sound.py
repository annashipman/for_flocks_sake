# This is the sound class

# For handling filenames... 
import os
# The pygame module itself..
import pygame

class sound:
	def __init__(self,soundFile):
            self.filePath = os.path.join('res/audio', soundFile)
            self.sound = pygame.mixer.Sound(self.filePath)

	#Play the sound
	def playSound(self,channel):
            channel.play(self.sound)

	#Pause sound
	def pauseSound(self):
            self.sound.pause()

	#Un pause sound
	def unPauseSound(self):
            self.sound.unpause()
		
	#Fade out sound
	def fadeOutSound(self,time):
            self.sound.fadeout(time)

	#set sound volume
	def setVolume(self,volume):
            self.sound.set_volume(volume)

	#get sound volume
	def getVolume(self):
            return self.sound.get_volume()

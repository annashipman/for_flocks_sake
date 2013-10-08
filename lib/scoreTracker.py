from State import State
import time

class Score:
    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state
	
    def setup(self):
        self.reset()
	
    def reset(self):
        self.score = 0
        self.scorePerBird = 9
        self.start_time = time.time()

    def scoreUpdateDrop(self, numberOfBirds):
        self.score += 1073 * numberOfBirds
        return self.score

    def scoreUpdate(self):
        now = time.time()
        if now - self.start_time < 1.0:
            return
        self.start_time = now
        scorePerFlockBird = 9
        flockSize = len(State().flock)

        if flockSize == 1 and flockSize < 9:
        	scorePerFlockBird = 0.03
        elif flockSize > 9 and flockSize < 15:
        	scorePerFlockBird = 0.1
        elif flockSize > 14 and flockSize < 20:
        	scorePerFlockBird = 0.16
        elif flockSize > 20:
        	scorePerFlockBird = 0.23

        self.score += self.scorePerBird * flockSize
        return self.score

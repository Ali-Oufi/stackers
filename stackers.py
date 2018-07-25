from sense_hat import SenseHat
from pygame.locals import *
import pygame
import time
import random
sense = SenseHat()
sense.clear()

class stack():
    def __init__(self):
        pygame.init()
        pygame.display.set_mode((640,480))
        self.gaming = True

    def startGame(self):
        pygame.time.set_timer(USEREVENT +1, 800)
        y = 0
        while self.gaming:
            for event in pygame.event.get():                 
                    sense.set_pixel(0, y, (0, 0, 255))
                    time.sleep(1)
                    sense.set_pixel(0, y, (0, 0, 0))
                    y += 1
                    if y == 8:
                        y = 0
                    
if __name__ == "__main__":
    try:
        game = stack()
        game.startGame()
    except KeyboardInterrupt:
        sense.clear()

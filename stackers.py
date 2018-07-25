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
        pygame.display.set_mode((200,200))
        self.gaming = True

    def startGame(self):
        pygame.time.set_timer(USEREVENT +1, 80)
        x = 0        
        y = 0
        velocity = 1
        while self.gaming:
            for event in pygame.event.get():                 
                    if event.type == KEYDOWN:
                        sense.set_pixel(x, y, (0, 0, 255))
                        self.gaming = False
                 #       x += 1
                    #    if x == 8:
                       #     self.gaming = False
                    else:
                        sense.set_pixel(x, y, (0, 0, 255))
                        time.sleep(0.05)
                        sense.set_pixel(x, y, (0, 0, 0))
                        y += velocity
                        if y == 8:
                            y = 0
                    
if __name__ == "__main__":
    try:
        game = stack()
        game.startGame()
    except KeyboardInterrupt:
        sense.clear()

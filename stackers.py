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
        pygame.time.set_timer(USEREVENT +1, 170)
        x = 0        
        y = 0
        previous_y = -1
        velocity = 1
        while self.gaming:
            for event in pygame.event.get():                 
                    if event.type == KEYDOWN:
                        if previous_y == -1:
                            previous_y = y
                        elif not (previous_y == y):
                            sense.show_message("You Lose!", 0.05, (255, 255, 0), (255, 0, 0))
                            self.gaming = False
                            sense.clear()
                            exit()
                        sense.set_pixel(x, y, (0, 0, 255))
                        x += 1
                        if x == 8:
                            sense.show_message("You Win!", 0.05, (255, 255, 0), (0, 0, 255))
                            self.gaming = False
                            sense.clear()
                            exit()
                    else:
                        sense.set_pixel(x, y, (0, 0, 255))
                        time.sleep(0.13)
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

import time
from sense_hat import SenseHat
sense = SenseHat()

yellow = (255,255,0)
blue = (0,0,255)
text_colour = yellow
back_colour = blue

speed = 0.05
message = 'Hello World'

sense.show_message(message, speed, text_colour, back_colour)
time.sleep(1)
sense.show_letter('!', yellow)
time.sleep(1)
sense.clear() 

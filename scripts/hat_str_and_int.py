from sense_hat import SenseHat
sense = SenseHat()
import time
red = (255,0,0)

i = 1
number = str(i)
sense.show_letter(number, red)
number = int(i)
time.sleep(number)

i += 1
number = str(i)
sense.show_letter(number, red)
number = int(i)
time.sleep(number)

sense.clear()

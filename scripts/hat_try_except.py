from sense_hat import SenseHat
import time

sense = SenseHat()
sense.clear()

def loop():
    while True:
        sense.set_pixel(1, 6, (255,140, 0))
        time.sleep(1)
        sense.set_pixel(1, 6, (255,20, 147))
        time.sleep(2)

if __name__ == "__main__":
    try:
        loop()
    except KeyboardInterrupt:
        sense.clear()

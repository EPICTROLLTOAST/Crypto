##cracke mersenne seed
import random
from Challenge21 import mersenne_twister
import time

time.sleep(random.randint(1, 1000))
ut = int(time.time())
rand = mersenne_twister(ut).randomNumber()
time.sleep(random.randint(1, 100))
currTime = int(time.time())

for x in range(currTime, currTime - 10000, -1):
    t = mersenne_twister(x)
    if t.randomNumber() == rand:
        assert ut == x
        print(f"The seed is {x}!")
        break




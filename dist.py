import math
from decimal import *

from Cryptodome.Util.number import getRandomNBitInteger

FLAG = "fake_flag"

# Python program to print prime factors

import math


# A function to print all prime factors of
# a given number n
def primeFactors(n):
    # Print the number of two's that divide n
    ret = []
    while n % 2 == 0:
        ret += [2]
        n = n // 2

    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used

    for i in range(3, int(math.sqrt(n)) + 1, 2):

        # while i divides n , print i ad divide n
        while n % i == 0:
            ret += [i]
            n = n // i

    # Condition if n is a prime
    # number greater than 2

    if n > 2:
        ret += [n]
    return ret



def is_perfect_square(n):
    lo = 1
    hi = n//2
    while lo < hi:
        mid = (lo+hi)//2
        if mid**2 == n:
            return True
        elif mid**2 < n:
            lo = mid+1
        else:
            hi = mid-1
    if lo**2 == n:
        return True
    else:
        return False

a = 0
while (a.bit_length() < 2048 or a < 0):
    k = getRandomNBitInteger(1024)
    my_y = getRandomNBitInteger(512)
    my_x = getRandomNBitInteger(512)
    a = k*(my_y**2) - (k-1)*(my_x**2)
    

print("Let's collaborate on a key!")
print("My x:", my_x)
print("My y:", my_y)
print("k:", k)
print("a:", a)

x = my_x ** 2 + my_y **3
alpha = my_y ** 2 // k
alpha_factors = primeFactors(alpha)
print(alpha_factors)



if (x.bit_length() < 1024):
    print("Sorry, your x needs to be long enough :(")
else:
    sq_y = ((k-1)*x**2 + a)//k
    if is_perfect_square(sq_y):
        print("Key collaboration successful! Here's the flag", FLAG)
    else:
        print("Sorry, the y obtained isn't valid :(")
    

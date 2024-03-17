
class mersenne_twister:
    def __init__(self, seed = 5489):
        self.w, self.n, self.m, self.r = 32, 624, 397, 31  # defining coefficients for MT 19937-64 bit
        self.f = 1812433253
        self.a = 0x9908B0DF
        self.u, self.d = 11, 0xFFFFFFFF
        self.s, self.b = 7, 0x9D2C5680
        self.t, self.c = 15, 0xEFC60000
        self.l = 18
        self.index = -1
        self.state = list() ##init the array
        self.state.append(seed)

        self.generateNumbers()
        # masks (to apply with an '&' operator)
        # ---------------------------------------
        # zeroes out all bits except "the w-r highest bits"
        # (i.e. with our parameters the single highest bit, since w-r=1)
        self.high_mask = ((1 << self.w) - 1) - ((1 << self.r) - 1)
        # zeroes out all bits excepts "the r lowest bits"
        self.low_mask = (1 << self.r) - 1



    def twist(self, x):
        return (x >> 1) ^ self.a if (x % 2 == 1) else x >> 1



    def generateNumbers(self):
        for i in range(1, self.n):
            prev = self.state[-1]
            x = (self.f * (prev ^ (prev >> (self.w - 2))) + i) & self.d  ##Given formula for genning the numbers in the array\
            self.state.append(x)


    def randomNumber(self):
        x = self.state[self.m] ^ self.twist((self.state[0] & self.high_mask) + (self.state[1] & self.low_mask)) ##by popping and indenting every time, the value of k gets indented

        self.state.pop(0)
        self.state.append(x) ##adding to state
        y = x ^ ((x >> self.u) & self.d)
        y = y ^ ((y << self.s) & self.b)
        y = y ^ ((y << self.t) & self.c)
        z = y ^ (y >> self.l)  ##algorithm defined by wikipedia where x is next value in list, y is an intermediate value and z is the value to return
        return z

if __name__ == '__main__':
    test_data = open('data/21.txt', 'r').read().split("\n")

    seed = 5489
    mt = mersenne_twister(seed)
    g = [mt.randomNumber() for x in range(len(test_data))]
    for x, y in zip(g, test_data):
        assert x == int(y)
    ##It works! I only copied a bit too! Only for the twist thing and the random number generator cos wikipedia said nothing bout that


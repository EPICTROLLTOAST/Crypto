# x = self.state[self.m] ^ self.twist((self.state[0] & self.high_mask) +
#             (self.state[1] & self.low_mask))  ##by popping and indenting every time, the value of k gets indented
#
# self.state.pop(0)
# self.state.append(x)  ##adding to state
#
# y = x ^ ((x >> self.u) & self.d)
# y = y ^ ((y << self.s) & self.b)
# y = y ^ ((y << self.t) & self.c)
# z = y ^ (y >> self.l)  ##algorithm defined by wikipedia where x is next value in list, y is an intermediate value and z is the value to return
# return z
from Set3.Challenge21 import mersenne_twister


class mersenne_break:
    def __init__(self):
        self.w, self.n, self.m, self.r = 32, 624, 397, 31  # defining coefficients for MT 19937-64 bit
        self.f = 1812433253
        self.a = 0x9908B0DF
        self.u, self.d = 11, 0xFFFFFFFF
        self.s, self.b = 7, 0x9D2C5680
        self.t, self.c = 15, 0xEFC60000
        self.l = 18
        self.state = [0 for x in range(self.n)]
        self.k = 0
        self.rng = None

    def twist(self, x):
        return (x >> 1) ^ self.a if (x % 2 == 1) else x >> 1

    def untemper(self, z):
        y3_first_18_bits = z & 0b11111111111111111100000000000000  ##First 18 bits
        y3_last_14_bits = (z & 0b00000000000000000011111111111111) ^ (y3_first_18_bits >> 18)
        y3 = y3_first_18_bits + y3_last_14_bits

        y2_NANDc = y3 & (0xFFFFFFFF - self.c)
        y2_16th_to_30th_bits = (y2_NANDc & 0b00000000000000011111111111111100) << 15
        y2 = (y2_16th_to_30th_bits & self.c) ^ y3

        y1_NANDb = y2 & (0xFFFFFFFF - self.b)
        y1_last_7_bits = y1_NANDb & 0b00000000000000000000000001111111
        y1_last_14_bits_and_b = ((y1_last_7_bits << 7) & self.b) ^ (y2 & self.b)
        y1_last_14_bits = (y1_NANDb & 0b00000000000000000011111111111111) + y1_last_14_bits_and_b
        y1_last_21_bits_and_b = ((y1_last_14_bits << 7) & self.b) ^ (y2 & self.b)
        y1_last_21_bits = (y1_NANDb & 0b00000000000111111111111111111111) + y1_last_21_bits_and_b  ##valid up to this point
        y1_last_28_bits_and_b = ((y1_last_21_bits << 7) & self.b) ^ (y2 & self.b)
        y1_last_28_bits = (y1_NANDb & 0b00001111111111111111111111111111) + y1_last_28_bits_and_b  ##probably only accurate for last 25 bits
        y1_last_25_bits = y1_last_28_bits & 0b00000001111111111111111111111111
        y1_and_b = (y2 & self.b) ^ ((y1_last_25_bits << 7) & self.b)
        y1 = y1_and_b + y1_NANDb

        x_first_11_bits = y1 & (0b11111111111 << 21)
        x_first_22_bits = x_first_11_bits + ((y1 & (0b11111111111 << 10)) ^ ((x_first_11_bits >> 11) & (0b11111111111 << 10)))
        x = y1 ^ (x_first_22_bits >> 11)
        self.state[self.k] = x
        self.k += 1

    def predict_next(self):
        assert self.k == self.n
        if self.rng is None:
            self.rng = mersenne_twister()
            self.rng.state = self.state
        return self.rng.randomNumber()


mt = mersenne_twister(seed=101010)
mb = mersenne_break()
for x in range(624):
    random = mt.randomNumber()
    mb.untemper(random)

print(mt.randomNumber())
print(mb.predict_next())

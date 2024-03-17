import os
import random

from Crypto.Random import get_random_bytes

from Set3.Challenge21 import mersenne_twister


class mtStreamCipher():
    def __init__(self, key=0):
        self.key = key
        self.mt = None

    def encrypt(self, p: bytes):
        self.mt = mersenne_twister(self.key)
        stream = []
        cipher = b""
        for x, y in enumerate(p):
            if x > len(stream) - 1:
                stream += self.mt.randomNumber().to_bytes(4, 'big')
            cipher += (y ^ stream[x]).to_bytes(1, 'big')
        return cipher

    def decrypt(self, c):
        self.mt = mersenne_twister(self.key)
        stream = []
        plaintext = b""
        for x, y in enumerate(c):
            if x > len(stream) - 1:
                stream += self.mt.randomNumber().to_bytes(4, 'big')
            plaintext += (y ^ stream[x]).to_bytes(1, 'big')
        return plaintext




if __name__ == '__main__':
    maxSeed = (1 << 16) - 1
    sc = mtStreamCipher(key = random.randint(0, maxSeed))

    plaintext = get_random_bytes(8) + b"AAAAAAAAAAAAAA"
    cipher = sc.encrypt(plaintext)
    for x in range(maxSeed):
        mt = mtStreamCipher(x)
        toEncrypt = b"1" * 8 + b"A" * 14
        if cipher[8:] == mt.encrypt(toEncrypt)[8:]:
            print(f"Seed is {x}")
            break

##Part two of challenge

if __name__ == '__main__':
    pass


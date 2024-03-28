import itertools
import random

from Cryptodome.Cipher import AES

from Set2.Challenge9_PKCS import PKCS_pad
from scipy.stats import shapiro


def randomKeyGen():
    r = b"".join(random.randint(0, 255).to_bytes(1, 'big') for x in range(16))
    return r


def encryption_oracle(_in: bytes):
    length = len(_in) + 10
    _in = b"".join(random.randint(0, 255).to_bytes(1, 'big') for x in range(5)) + _in + b"".join(
        random.randint(0, 255).to_bytes(1, 'big') for x in range(5))  ##padding
    if length % 16 != 0:
        _in = PKCS_pad(_in, length - length % 16 + 16)
    key = randomKeyGen()
    cipher = ""
    mode = "CBC"
    if random.randint(1, 2) == 1:  ##ECB
        aes = AES.new(key, AES.MODE_ECB)
        cipher = aes.encrypt(_in)
        print("ECB")
        mode = "ECB"
    else:
        IV = randomKeyGen()
        aes = AES.new(key, AES.MODE_CBC, IV=IV)
        cipher = aes.encrypt(_in)
        print("CBC")

    return cipher, mode


def detector(cipher):
    dic = [x for x in cipher]
    counts = sum(dic)
    mean = counts/256
    ##carrying out the Shapiro-wilk test

    results = shapiro(dic)
    return results.pvalue

ecb = []
cbc = []


cipher = encryption_oracle(open("Data/Rolling.txt", "r").read().encode())
blocks = [cipher[0][x:x+16] for x in range(0, len(cipher[0]), 16)]
pairs = itertools.combinations(blocks, 2)
count = 0
for p in pairs:

    if p[0] == p[1]:
        count += 1

if count >= 1:
    print("Probably a ECB")
else:
    print("Probably a CBC")
print(count)
print(cipher[1])
##detect AES_ECB
import base64
import itertools

from Cryptodome.Cipher import AES

_in = open("Data/8.txt", "r").read().split("\n")
_in = [base64.b16decode(x.upper()) for x in _in]
ls = []
line = 0
for y in _in:
    chunks = [y[x:x+16] for x in range(0, len(y), 16)]
    pairs = itertools.combinations(chunks, 2)
    score = 0
    for p in pairs:
        if p[0] == p[1]:
            score += 1
    line += 1
    ls += [[score, y, line]]
for x in ls:
    if x[0] > 0:
        print(x)
        print(x[1], " is probably the once encrypted by aes in ecb")
        print("it's line number is ", x[2])




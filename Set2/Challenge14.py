import base64
import random

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

from Set2.Challenge9_PKCS import PKCS_pad

key = get_random_bytes(16)
toPrepend = get_random_bytes(random.randint(1, 100))
aes = None


def AES_128_ECB(_in):
    global key
    global aes

    _n = base64.b64decode(b"""Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkg
    aGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBq
    dXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUg
    YnkK""")
    _in = toPrepend + _in + _n

    if aes is None:
        aes = AES.new(key, AES.MODE_ECB)

    lengthOfPlaintext = len(_in) + 10
    _in = _in  ##padding
    _in = PKCS_pad(_in, 16)

    cipher = aes.encrypt(_in)

    return cipher


prevBlock = b"A"
length = 0
prevPrevBlockSize = 0
prevBlockSize = len(AES_128_ECB(b"A" * length))
print(prevBlockSize)
while prevBlockSize == len(AES_128_ECB(b"A" * length)):
    prevBlockSize = len(AES_128_ECB(b"A" * length))
    length += 1

print(f"Block size is {len(AES_128_ECB(b'A' * length)) - prevBlockSize}")
blockSize = len(AES_128_ECB(b'A' * length)) - prevBlockSize
knownSize = 0

prePad = b"A" * 3 * blockSize

result = AES_128_ECB(prePad)
blocks = [result[x:x + blockSize] for x in range(0, len(result), blockSize)]

posAtAEndPadding = 0
prevBlock = b""
for x in blocks:
    if prevBlock == x:
        posAtAEndPadding += blockSize
        break
    else:
        posAtAEndPadding += blockSize
        prevBlock = x

_1 = AES_128_ECB(prePad + b"A")[posAtAEndPadding - blockSize : posAtAEndPadding]
_1_ = AES_128_ECB(prePad + b"A")
_2 = AES_128_ECB(prePad)[posAtAEndPadding - blockSize :posAtAEndPadding]
_2_ = AES_128_ECB(prePad)


if _1 != _2: ##Blocks perfectly padded
    posAtAEndPadding += blockSize

else:
    decrLen = 1
    prePad = b"A" * (3 * blockSize - decrLen)
    _1 = AES_128_ECB(prePad + b"A")[posAtAEndPadding - blockSize : posAtAEndPadding]
    _1_ = AES_128_ECB(prePad + b"A")
    _2 = AES_128_ECB(prePad)[posAtAEndPadding - blockSize :posAtAEndPadding]
    _2_ = AES_128_ECB(prePad)
    True
    while _1 == _2:
        decrLen += 1

        prePad = b"A" * (3 * blockSize - decrLen)
        _1 = AES_128_ECB(prePad + b"A")[posAtAEndPadding - blockSize: posAtAEndPadding]
        _1_ = AES_128_ECB(prePad + b"A")
        _2 = AES_128_ECB(prePad)[posAtAEndPadding - blockSize:posAtAEndPadding]
        _2_ = AES_128_ECB(prePad)
    prePad += b"A"

startIndexOfProper = posAtAEndPadding

blocks = len(AES_128_ECB(b"")) // blockSize

toInput = b"A" * blockSize
end2 = b""

for z in range(startIndexOfProper // blockSize, len(AES_128_ECB(prePad + toInput)) // blockSize - 1):
    knownSize = 0
    end = b""
    for x in range(blockSize):
        poss = []

        for y in range(256):
            to = prePad + toInput[1 + knownSize:] + end + y.to_bytes(1, 'big')
            poss += [AES_128_ECB(to)[posAtAEndPadding :posAtAEndPadding + blockSize]] ##simulation of all possibilities
        to = prePad + toInput[1 + knownSize:]
        one_byte_short = AES_128_ECB(to)[blockSize * z : blockSize * (z + 1)]
        result = chr(poss.index(one_byte_short))
        end += result.encode()
        knownSize += 1
        print(end)
    toInput = end
    end2 += end
print(end2)

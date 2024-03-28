import base64
import random

from Cryptodome.Cipher import AES

from Challenge9_PKCS import PKCS_pad


def randomKeyGen():
    r = b"".join(random.randint(0, 255).to_bytes(1, 'big') for x in range(16))
    return r


key = b""
aes = None

def AES_128_ECB(_in):
    global key
    global aes

    _n = base64.b64decode(b"""Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkg
    aGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBq
    dXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUg
    YnkK""")
    _in += _n
    if len(key) == 0:
        print("generating key")
        key = randomKeyGen()
    if aes == None:
        aes = AES.new(key, AES.MODE_ECB)

    lengthOfPlaintext = len(_in) + 10
    _in = _in ##padding
    _in = PKCS_pad(_in, lengthOfPlaintext - lengthOfPlaintext % 16 + 16)

    ##always uses ecb

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



blocks = len(AES_128_ECB(b""))//blockSize
toInput = b"A" * blockSize
end2 = b""

for z in range(blocks):
    knownSize = 0
    end = b""
    for x in range(blockSize):
        poss = []

        for y in range(256):
            to = toInput[1 + knownSize:] + end + y.to_bytes(1, 'big')
            poss += [AES_128_ECB(to)[:blockSize]]
        to = toInput[1 + knownSize:]
        one_byte_short = AES_128_ECB(to)[blockSize * z:blockSize * (z + 1)]
        result = chr(poss.index(one_byte_short))
        end += result.encode()
        knownSize += 1
        print(end)
    toInput = end
    end2 += end
print(end2)





from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes

from Set2.Challenge9_PKCS import PKCS_pad

key = get_random_bytes(16)
IV = get_random_bytes(16)


def CBCOracle(_in: str):
    global IV
    global key
    aes = AES.new(key, AES.MODE_CBC, IV=IV)
    _in = _in.replace(";", "")
    _in = _in.replace("=", "")
    fin = PKCS_pad(("comment1=cooking%20MCs;userdata=" + _in + ";comment2=%20like%20a%20pound%20of%20bacon").encode(), 16)
    return aes.encrypt(fin)


def decrypt(_in: bytes):
    global IV
    global key
    aes = AES.new(key, AES.MODE_CBC, IV=IV)
    return aes.decrypt(_in)


def getUserProf(_in):
    x = decrypt(_in)
    print(x)
    if b";admin=true;" in x:
        print("Wow this guy is an admin, what a big-shot!")



blockSize = 16
standard = bytearray(CBCOracle("A"* blockSize * 2)) ##For two blocksize of A


blocks = [standard[x:x+blockSize] for x in range(0, len(standard), blockSize)]

xors = []
intended = "AAAAA;admin=true"
for x, y in zip(b"AAAAAAAAAAAAAAAA", intended):
    xors += [x ^ ord(y)]
for x in range(32, 32 + blockSize):
    standard[x] ^= xors[x - 32]


print(standard)
print(decrypt(standard))
blocks = [decrypt(standard)[x:x+blockSize] for x in range(0, len(standard), blockSize)]
print(blocks)
getUserProf(standard)
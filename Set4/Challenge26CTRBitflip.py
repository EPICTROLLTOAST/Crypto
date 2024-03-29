from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes

from Set2.Challenge9_PKCS import PKCS_pad
IV = get_random_bytes(1)
key = get_random_bytes(16)
##change to ctr

def CTROracle(_in: str):
    global key
    aes = AES.new(key, AES.MODE_CTR, nonce=IV)
    _in = _in.replace(";", "")
    _in = _in.replace("=", "")
    fin = PKCS_pad(("comment1=cooking%20MCs;userdata=" + _in + ";comment2=%20like%20a%20pound%20of%20bacon").encode(), 16)


    return aes.encrypt(fin)


def decrypt(_in: bytes):
    global IV
    global key
    aes = AES.new(key, AES.MODE_CTR, nonce=IV)
    return aes.decrypt(_in)


def getUserProf(_in):
    x = decrypt(_in)
    print(x)
    if b";admin=true;" in x:
        print("Wow this guy is an admin, what a big-shot!")



blockSize = 16
standard = bytearray(CTROracle("A"* blockSize * 2)) ##For two blocksize of A


blocks = [standard[x:x+blockSize] for x in range(0, len(standard), blockSize)]

xors = []
intended = "AAAAA;admin=true"
for x, y in zip(b"AAAAAAAAAAAAAAAA", intended):
    xors += [x ^ ord(y)]
for x in range(48, 48 + blockSize):
    standard[x] ^= xors[x - 48]


print(standard)
print(decrypt(standard))
blocks = [decrypt(standard)[x:x+blockSize] for x in range(0, len(standard), blockSize)]
print(blocks)
getUserProf(standard)
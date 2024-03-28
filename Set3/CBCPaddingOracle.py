import base64
import random

from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes

from Set2.Challenge9_PKCS import PKCS_pad, PKCS_validate

strings = [base64.b64decode(x) for x in """MDAwMDAwTm93IHRoYXQgdGhlIHBhcnR5IGlzIGp1bXBpbmc=
MDAwMDAxV2l0aCB0aGUgYmFzcyBraWNrZWQgaW4gYW5kIHRoZSBWZWdhJ3MgYXJlIHB1bXBpbic=
MDAwMDAyUXVpY2sgdG8gdGhlIHBvaW50LCB0byB0aGUgcG9pbnQsIG5vIGZha2luZw==
MDAwMDAzQ29va2luZyBNQydzIGxpa2UgYSBwb3VuZCBvZiBiYWNvbg==
MDAwMDA0QnVybmluZyAnZW0sIGlmIHlvdSBhaW4ndCBxdWljayBhbmQgbmltYmxl
MDAwMDA1SSBnbyBjcmF6eSB3aGVuIEkgaGVhciBhIGN5bWJhbA==
MDAwMDA2QW5kIGEgaGlnaCBoYXQgd2l0aCBhIHNvdXBlZCB1cCB0ZW1wbw==
MDAwMDA3SSdtIG9uIGEgcm9sbCwgaXQncyB0aW1lIHRvIGdvIHNvbG8=
MDAwMDA4b2xsaW4nIGluIG15IGZpdmUgcG9pbnQgb2g=
MDAwMDA5aXRoIG15IHJhZy10b3AgZG93biBzbyBteSBoYWlyIGNhbiBibG93""".split("\n")]


class CBCPaddingOracle:
    def __init__(self):
        self.key = get_random_bytes(16)
        self.IV = get_random_bytes(16)

    def oracle(self) -> (bytes, bytes):
        global strings
        return AES.new(key=self.key, IV=self.IV, mode=AES.MODE_CBC).encrypt(
            PKCS_pad(random.choice(strings), 16)), self.IV

    def decrypt(self, _in):
        try:
            decrypted = AES.new(key=self.key, IV=self.IV, mode=AES.MODE_CBC).decrypt(_in)
            PKCS_validate(decrypted, 16)
            return True
        except:
            return False


blockSize = 16
oracle = CBCPaddingOracle()
out = oracle.oracle()
cipher = bytearray(out[1] + out[0])
iv = out[1]
blocks = [cipher[x: x + blockSize] for x in range(0, len(cipher), 16)]
findLastPadding = 0

out2 = b""
for blockNumber in range(0, len(blocks) - 1):
    padSize = 0x01
    out = b""
    for z in range(blockSize):
        y = 1
        flag = True ##break flag
        while y < 256 and flag:
            if -blockSize * blockNumber == 0:
                cipherCopy = cipher.copy()
            else:
                cipherCopy = cipher.copy()[:-blockSize * blockNumber]
            for x, k in zip(range(len(cipherCopy) - 1 - blockSize, len(cipherCopy) -1 -blockSize - z, -1), out[::-1]): ##iterates from end to just before the test
                cipherCopy[x] ^= k ##This xors the next block with itself
                cipherCopy[x] ^= padSize ##Then sets the end byte to ahve to be the padding

            cipherCopy[-1 - blockSize - z] ^= y ##This just modifies the zth last byte of the last block

            if oracle.decrypt(cipherCopy):
                out = (y ^ padSize).to_bytes(1, 'big') + out
                padSize += 1
                print(out)
                flag = False ## break out of the loop

            y += 1
            if y == 256: ##if you tried all other poss combinations it must be 0x00
                out += (0x00 ^ padSize).to_bytes(1, 'big')
                padSize += 0x01
    out2 = out + out2

print(out2)

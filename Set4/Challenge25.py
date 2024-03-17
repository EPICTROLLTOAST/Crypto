import base64

from Set3.Challenge18_CTR import aes_128_ctr_keystream_generator, aes_128_ctr_transform

class randomAccessAESCTR:
    def __init__(self, plaintext, key = b"0123456789ABCDEF", nonce = 0):
        self.key = key
        self.nonce = nonce
        self.cipher = b"".join((x ^ y).to_bytes(1, 'big') for x, y in zip(aes_128_ctr_keystream_generator(key, nonce), plaintext))

    def edit(self, offset, newText:bytes):
        assert offset + len(newText) <= len(self.cipher)
        relGen = [x for x, y in zip(aes_128_ctr_keystream_generator(self.key, self.nonce), range(len(self.cipher)))][offset:offset + len(newText)]
        toInsert = b""
        for x, y in zip(newText, relGen):
            toInsert += (x ^ y).to_bytes(1, 'big')
        self.cipher = self.cipher[:offset] + toInsert + self.cipher[offset + len(toInsert):]

    def decrypt(self):
        return aes_128_ctr_transform(self.cipher, self.key, self.nonce)


raCTR = randomAccessAESCTR(b"Umm Actually", key = b"YELLOW SUBMARINE", nonce = 1)
cipher = raCTR.cipher
raCTR.edit(0, b"\x00" * len(cipher))
keyStream = raCTR.cipher

print("".join(chr(x ^ y) for x, y in zip(keyStream, cipher)))

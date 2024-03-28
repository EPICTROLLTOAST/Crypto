import base64

from Cryptodome.Cipher import AES

##WARNING
## for some reason the transform is corrupted as fuck, prob because of the fact that its prob gon be encoding in utf

def aes_128_ctr_keystream_generator(key, nonce):
    counter = 0
    while True:
        to_encrypt = (nonce.to_bytes(length=8, byteorder='little')
                      + counter.to_bytes(length=8, byteorder='little'))
        keystream_block = AES.new(key = key, mode = AES.MODE_ECB).encrypt(to_encrypt)
        # equivalent to "for byte in keystream_block: yield byte"
        # for the "yield" keyword in Python,
        # see https://docs.python.org/3/tutorial/classes.html#generators
        yield from keystream_block

        counter += 1


def aes_128_ctr_transform(msg, key, nonce) -> bytes:
    '''does both encryption (msg is plaintext)
    and decryption (msg is ciphertext)'''

    keystream = aes_128_ctr_keystream_generator(key, nonce)
    return ("".join(chr(x ^ y) for x, y in zip(msg, keystream))).encode()

if __name__ == '__main__':
    ctxt = base64.b64decode('L77na/nrFsKvynd6HzOoG7GHTLXsTVu9qvY/2syLXzhPweyyMTJULu/6/kXX0KSvoOLSFQ==')
    print(aes_128_ctr_transform(ctxt, key=b'YELLOW SUBMARINE', nonce=0))

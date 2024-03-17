import os
from base64 import b64decode
from itertools import zip_longest

from Set3.Challenge18_CTR import aes_128_ctr_transform


##I copied code yet it still didnt work, I'm guessing sample isn't big enough to get anything reliable


def bxor(a, b, longest=True):
    if longest:
        return bytes([x ^ y for (x, y) in zip_longest(a, b, fillvalue=0)])
    else:
        return bytes([x ^ y for (x, y) in zip(a, b)])


def attack_single_byte_xor(ciphertext):
    ascii_text_chars = list(range(97, 122)) + [32]
    # a variable to keep track of the best candidate so far
    best = None
    secondBest = None
    for i in range(2 ** 8):  # for every possible key
        # converting the key from a number to a byte
        candidate_key = i.to_bytes(1, byteorder='big')
        keystream = candidate_key * len(ciphertext)
        candidate_message = bxor(ciphertext, keystream)
        nb_letters = sum([x in ascii_text_chars for x in candidate_message])
        # if the obtained message has more letters than any other candidate before
        if best == None or nb_letters > best['nb_letters']:
            secondBest = best
            # store the current key and message as our best candidate so far
            best = {"message": candidate_message, 'nb_letters': nb_letters, 'key': candidate_key}

    return best, secondBest


with open('data/20.txt') as f:
    data = [b64decode(line) for line in f]

key = os.urandom(16)

ctxts = [aes_128_ctr_transform(line, key, 0)
         for line in data]

columns = [attack_single_byte_xor(l)[0]['message'] for l in zip(*ctxts)]

for msg in zip(*columns):
    print(bytes(msg).decode())

import base64
ascii_text_chars = list(range(97, 122)) + [32]

def score(s):
    freq = {}
    freq[' '] = 700000000
    freq['e'] = 390395169
    freq['t'] = 282039486
    freq['a'] = 248362256
    freq['o'] = 235661502
    freq['i'] = 214822972
    freq['n'] = 214319386
    freq['s'] = 196844692
    freq['h'] = 193607737
    freq['r'] = 184990759
    freq['d'] = 134044565
    freq['l'] = 125951672
    freq['u'] = 88219598
    freq['c'] = 79962026
    freq['m'] = 79502870
    freq['f'] = 72967175
    freq['w'] = 69069021
    freq['g'] = 61549736
    freq['y'] = 59010696
    freq['p'] = 55746578
    freq['b'] = 47673928
    freq['v'] = 30476191
    freq['k'] = 22969448
    freq['x'] = 5574077
    freq['j'] = 4507165
    freq['q'] = 3649838
    freq['z'] = 2456495
    freq["\b"] = -1000000000000
    freq["\t"] = -1000000000000
    freq["~"] = -10000000000000
    freq["ø"] = -10000000000000
    freq[""] = -1000000000000
    freq["*"] = -1000000000000

    score = 0
    for c in s.lower():
        if c in freq:
            score += freq[c]
        else:
            if  192 < ord(c) < 238:
                score -= 100000000000
            if c in "^[]\\_":
                score -= 100000000000
            score -= 10000
    return score


def hammingDistance(a: bytes, b: bytes):
    dist = 0
    if len(a) != len(b):
        raise "Oi! a nd b is not the same length!"

    for x, y in zip(a, b):
        xb = bin(x)[2:].zfill(8) ##assuming hex
        yb = bin(y)[2:].zfill(8)

        for _1, _2 in zip(xb, yb):
            if _1 != _2: dist += 1
    return dist

def breakSingleKeyXOR(cipher:bytes):
    ls = []
    corrPlain = []
    for z in range(256):
        key = [z] * len(cipher)

        plain = "".join(chr(x ^ y) for x, y in zip(cipher, key))
        ls += [score(plain)]
        corrPlain += [plain]
    cipher = "".join((chr(x) for x in cipher))
    plain = corrPlain[ls.index(max(ls))]
    key = chr(ls.index(max(ls)))
    return key






if __name__ == '__main__':
    _in = """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"""


    _in = base64.b64decode(_in)
    small = 2
    big = 40


    normalised_distances = []
    for x in range(small, big):
        b1 = _in[0:x]
        b2 = _in[x: x * 2]
        b3 = _in[x*2:x*3]
        b4 = _in[x*3:x*4]
        normalised_distance = (hammingDistance(b1,b2) + hammingDistance(b2,b3) + hammingDistance(b3,b4))/x
        normalised_distances += [[normalised_distance, x]]
    normalised_distances = sorted(normalised_distances, key = lambda index:index[0])
    print(normalised_distances)

    for stuff in normalised_distances[:5]: #top 5
        size = stuff[1]
        blocks = []
        for x in range(0, len(_in), size):
            if x + size >= len(_in): ##exceeds the length
                blocks += [_in[x:]]
            else:
                blocks += [_in[x: x+size]]

        transposed = []

        for x in range(size):
            transposed += [[]]
            for y in range(len(blocks)):
                if len(blocks[y]) > x:
                    transposed[x] += [blocks[y][x]]

        key = ""
        for x in transposed:
            key += breakSingleKeyXOR(x)

        key *= len(_in) // len(key)
        if len(key) - len(_in) % len(key) != 0:
            key += key[0:len(_in) % len(key)]
        print(key)

        out = ""
        for x, y in zip(_in, key):
            out += chr(x ^ ord(y))
        print(out)

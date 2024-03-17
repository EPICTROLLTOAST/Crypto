import base64


def padMod(s, mod, char="0", left=True):
    toRet = ""
    remainder = len(s) % mod

    for x in range(remainder):
        toRet += char
        if left:
            toRet += s
        else:
            toRet = s + toRet
    return toRet


def scorer(s:str) -> float:
    common = "ETAOIN SHRDLU"
    ok = "1234567890QWERTYUIOPASDFGHJKLZXCVBNM\'\".,!?"
    tot = 0
    for x in s:
        if x.upper() in common:
            tot += 5
        elif x.upper() in ok:
            tot += 1
        else:
            tot -= 100
    return tot


if __name__ == "__main__":

    ls = []
    _in = base64.b16decode(b"1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736".upper())
    for z in range(256):
        key = base64.b16decode(base64.b16encode(z.to_bytes(1, 'big')))
        k = (key * int(len(_in)/2))
        out = "".join(chr(x^y) for x,y in zip(_in, k))
        ls += [out]

    print(ls)
    m = -1
    curr = ""
    for x in ls:
        if scorer(x) > m:
            m = scorer(x)
            curr = x
    print(curr)



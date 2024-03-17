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

ls = []


_in = []

for x in open("Data/4.txt", "r").read().split("\n"):
    s = x.upper()
    s = "0" + s if len(s) % 2 == 1 else s
    _in += [base64.b16decode(s)]
    print(s)

for x in _in:
    for z in range(256):
        key = base64.b16decode(base64.b16encode(z.to_bytes(1, 'big')))
        k = (key * int(len(x)/2))
        out = "".join(chr(xs ^ y) for xs,y in zip(x, k))
        ls += [out]

m = -9999999999
curr = ""
for x in ls:
    if scorer(x) > m:
        m = scorer(x)
        curr = x
print(curr)

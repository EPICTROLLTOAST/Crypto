key = "CYLAB"
_in = b"yrgnoDVD{O0NU_WQ3_G1G3O3T3_A1AH3S_f85729e7}"

key *= len(_in) // len(key)
if len(key) - len(_in) % len(key) != 0:
    key += key[0:len(_in) % len(key)]
print(key)

out = ""
for x, y in zip(_in, key):
    out += chr(x ^ ord(y))
print(out)
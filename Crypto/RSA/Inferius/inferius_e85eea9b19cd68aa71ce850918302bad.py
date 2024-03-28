#!/usr/bin/env python3

from Cryptodome.Util.number import getPrime, inverse, bytes_to_long, long_to_bytes, GCD

e = 3

# n will be 8 * (100 + 100) = 1600 bits strong which is pretty good
while True:
    p = getPrime(100)
    q = getPrime(100)
    phi = (p - 1) * (q - 1)
    try:
        d = pow(e, -1, phi)
    except:
        d = -1
    if d != -1 and GCD(e, phi) == 1:
        break

n = p * q

flag = b"XXXXXXXXXXXXXXXXXXXXXXX"
pt = bytes_to_long(flag)
ct = pow(pt, e, n)

print(f"n = {n}")
print(f"e = {e}")
print(f"ct = {ct}")

pt = pow(ct, d, n)
decrypted = long_to_bytes(pt)
assert decrypted == flag

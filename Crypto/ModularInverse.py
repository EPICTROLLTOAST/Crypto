import math

_in = "104 372 110 436 262 173 354 393 351 297 241 86 262 359 256 441 124 154 165 165 219 288 42"
for x in (_in).split(" "):
    alphabet = "abcdefghijklmnopqrstuvwxyz0123456789_"
    y = int(x) % 41
    y = pow(y, -1, 41) - 1
    y = y % 37
    print(alphabet[y], end = "")
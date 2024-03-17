import base64
import Challenge1


def verify(_1, _2):
    if _1 == _2:
        print("Facts")
        print(f"{_1} is equals to {_2}")
    else:
        print("Wrong!")
        print(f"{_1} is not equals to {_2}")


_in = base64.b16decode(b"1c0111001f010100061a024b53535009181c".upper())
key = base64.b16decode(b"686974207468652062756c6c277320657965".upper())

_out = ""
for x, y in zip(_in, key):
    _out += chr(x ^ y)

print(_out)

verify("746865206b696420646f6e277420706c6179", _out)

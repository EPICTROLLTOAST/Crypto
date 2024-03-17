import base64

def verify(_1, _2):
    if _1 == _2:
        print("Facts")
        print(f"{_1} is equals to {_2}")
    else:
        print("Wrong!")
        print(f"{_1} is not equals to {_2}")




if __name__ == "__main__":
    b64 = base64.b64encode(base64.b16decode(b"49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d".upper()))

    verify(b64, b"SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t")

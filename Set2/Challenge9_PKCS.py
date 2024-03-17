







def PKCS_pad(b: bytes, padTo: int) -> bytes:
    multi = padTo
    firstPass = True
    while padTo <= len(b):
        padTo += multi
        firstPass = False

    b += chr(padTo - len(b)).encode() * (padTo - len(b))
    return b

def PKCS_validate(_in : bytes, blockSize : int):
    prevX = "\x04"
    copy = _in[len(_in) - blockSize:]
    if len(copy) != blockSize:
        raise "Error! It's not of appropriate blocksize"
    end = ""
    timesPadded = _in[-1]
    if timesPadded < 0x01 or timesPadded > 0x10:
        raise "Error last byte cannot be  < 0x01 or > 0x10"
    for x in range(len(_in) - 1, len(_in) - 1 - timesPadded, -1):
        if _in[x] != timesPadded:
            raise "Oi! Improper PKCS padding"
    return _in[:-timesPadded]


if __name__ == '__main__':
    print(PKCS_validate(b"0123456789\x06\x06\x06\x06\x06\x01", 16))

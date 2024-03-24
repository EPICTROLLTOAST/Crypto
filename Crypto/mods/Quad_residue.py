
def fastQuadResidue(mod :int, number :int) -> int:
    return pow(number, (mod - 1)//2, mod)


if __name__ == '__main__':
    p = 29
    ints = [14, 6, 11]
    for x in ints:
        for y in range(1, p - 1):
            if (y ** 2) % p == x % p:
                print(f"{x} is a quadratic residue of {y}")

    p = 101524035174539890485408575671085261788758965189060164484385690801466167356667036677932998889725476582421738788500738738503134356158197247473850273565349249573867251280253564698939768700489401960767007716413932851838937641880157263936985954881657889497583485535527613578457628399173971810541670838543309159139

    ints = []

    l = [fastQuadResidue(p, x) for x in ints]


    for index, x in enumerate(l):
        if x == 1:
            a = ints[index]
            ans1 = pow(a, (p + 1)//4, p)
            ans2 = -ans1

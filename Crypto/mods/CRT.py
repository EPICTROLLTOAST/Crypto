


def crt(eqn:[(int, int)], ap:(int, int) = None) -> int:
    if len(eqn) == 1:
        eqn = eqn[0]
        if ap == None:
            return eqn[0]
        else:
            n = 0
            while (ap[0] + ap[1] * n) % eqn[1] != eqn[0]:
                n += 1
            return ap[0] + ap[1] * n
    else:
        ap = None
        done = []
        prod = 1
        re = 0
        for index, x in enumerate(eqn):
            re = crt(eqn = [x], ap = ap)
            done += [x[1]]
            prod *= done[-1]

            ap = (re, prod)

        return re % prod


print(crt([(2, 5), (3, 11), (5, 17)]))
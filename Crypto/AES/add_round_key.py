from matrix import matrix2bytes




def add_round_key(s, k):
    m = []
    indice = -1
    for x, y in zip(k, s):
        m += [[]]
        indice += 1
        for i, j in zip(x, y):
            m[indice] += [i ^ j]
    print(m)
    return m


if __name__ == '__main__':
    state = [
        [206, 243, 61, 34],
        [171, 11, 93, 31],
        [16, 200, 91, 108],
        [150, 3, 194, 51],
    ]

    round_key = [
        [173, 129, 68, 82],
        [223, 100, 38, 109],
        [32, 189, 53, 8],
        [253, 48, 187, 78],
    ]

    print(matrix2bytes(add_round_key(state, round_key)))

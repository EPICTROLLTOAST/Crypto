import math
import numpy
from GramSchmidt import vector


def GLR(_1: vector, _2: vector) -> (vector, vector):
    v1 = _1
    v2 = _2

    while True:
        if v2.dot_product(v2) < v1.dot_product(v1):
            v1, v2 = v2, v1
        m = round(v1.dot_product(v2) / v1.dot_product(v1))
        if m == 0:
            return v1, v2
        v2 = v2 - (v1 * m)


r = GLR(vector([846835985, 9834798552]), vector([87502093, 123094980]))
print(r)
print(r[0].dot_product(r[1]))

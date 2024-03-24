from fractions import Fraction
from copy import deepcopy

from fractions import Fraction
from math import sqrt


##!! DISCLAIMER
##ALL THIS CODE WAS COPIED FROM https://github.com/pwang00/Gram-Schmidt-LLL/blob/master/vector.py
##I FUCKED UP MY FORMULA AND IT WAS TOO LATE FOR ME TO CARE

class vector(object):
    int_array = []
    magnitude = 0

    def __init__(self, v):
        if type(v) in [list, tuple]:
            self.int_array = [int(i) if int(i) == i else i for i in v]
        elif type(v) == vector:
            self.int_array = v.get_values()
        self.magnitude = sqrt(sum([v_i ** 2 for v_i in self.int_array]))

    def get_values(self):
        return self.int_array

    def __mul__(self, c):
        try:
            assert type(c) in [float, int]
        except:
            raise ValueError("c must be a scalar type")
        return vector([c * i for i in self.int_array])

    def __rmul__(self, c):
        try:
            assert type(c) in [float, int]
        except:
            raise ValueError("c must be a scalar type")
        return vector([c * i for i in self.int_array])

    def __iter__(self):
        return iter(self.int_array)

    def __iadd__(self, v):
        self.int_array = [v.get_values()[i] + self.int_array[i] for i in range(len(self.int_array))]
        return vector(self.int_array)

    def __add__(self, v):
        return vector([v.get_values()[i] + self.int_array[i] for i in range(len(self.int_array))])

    def __sub__(self, v):
        return vector([self.int_array[i] - v.get_values()[i] for i in range(len(self.int_array))])

    def __isub__(self, v):
        self.int_array = [self.int_array[i] - v.get_values()[i] for i in range(len(self.int_array))]
        return vector(self.int_array)

    def dot_product(self, v):
        assert len(v.get_values()) == len(self.int_array)
        return sum([v.get_values()[i] * self.int_array[i] for i in range(len(self.int_array))])

    def normalize(self):
        self.int_array = [v / self.magnitude for v in self.int_array]
        return vector(self.int_array)

    def fraction_form(self, denom_limit):
        return tuple([Fraction(i).limit_denominator(denom_limit) if int(i) != i else i for i in self.int_array])

    def __repr__(self):
        return repr(tuple(self.int_array))


def v_to_tex(v):
    u = []
    for i in v:
        u.append(str(i))
    return "\\langle" + ', '.join(u) + "\\rangle"


def vf_to_tex(v):
    u = []
    for f in v:
        u.append(f_to_tex(f))
    return "\\langle" + ', '.join(u) + "\\rangle"


def f_to_tex(f):
    return "\\frac{" + str(f.numerator) + "}{" + str(f.denominator) + "}" if f.denominator != 1 else str(f.numerator)


def gram_schmidt(*v, normalize=False, fraction=False, DENOM_LIMIT=100):
    # Check to see if argument is of type list
    if len(v) == 1 and type(v[0]) in [list, tuple]:
        v = v[0]

    if any([type(v_) != vector for v_ in v]):
        raise TypeError("Argument array must all be of type 'Vector'")

    # By Gram-Schmidt, w_1 = v_1
    w_1 = v[0]
    w_n = w_1
    w_array = [deepcopy(vector(w_n))]

    # Every vector w_1 ... w_n
    for n in range(1, len(v)):
        v_n = vector(v[n])
        w_n = vector(v_n)

        for j in range(n):
            w_j = deepcopy(w_array[j])
            if not any(w_j):
                continue
            w_n -= v_n.dot_product(w_j) / w_j.dot_product(w_j) * w_j

        w_array += [w_n]

    if fraction == True:
        w_array = [vector(w).fraction_form(DENOM_LIMIT) for w in w_array]

    if normalize == True:
        w_array = [vector(w).normalize() for w in w_array]

    return w_array


if __name__ == "__main__":
    print(gram_schmidt([vector([4, 1, 3, -1]), vector([2, 1, -3, 4]), vector([1, 0, -2, 7]), vector([6, 2, 9, -5])]))

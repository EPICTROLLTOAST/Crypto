a = 66528
b = 52920

while b != 0:
    a,b = (b, a%b)
print(a)

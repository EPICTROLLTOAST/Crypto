rk_1 = 26513
rk = 32321
q = 0
sk_1 = 1
sk = 0
tk_1 = 0
tk = 1

while rk != 0:
    q = rk_1 // rk
    rk_1, rk = rk, (rk_1 - q * rk)
    sk_1, sk = sk, (sk_1 - q * sk)
    tk_1, tk = tk, (tk_1 - q * tk)
print(f"GCD is {rk_1}")
print(f"coffs of bezout formula x = {sk_1}, y = {tk_1}")
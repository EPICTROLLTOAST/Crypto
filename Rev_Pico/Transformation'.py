rev_key = "灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸彥㜰㍢㐸㙽"
vals = [ord(x) for x in rev_key]
flag = ""
for x in vals:
    b = bin(x)[2:]
    print(b)
    second = str(int(b[7:]))
    second += "0" * (len(second) - len(second) % 7 if len(second)%7 != 0 else 0)
    flag += chr(int(b[:7], 2))
    flag += chr(int(second, 2))
print(flag)

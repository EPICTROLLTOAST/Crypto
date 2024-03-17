

s = "in"

blocks = [[s[y] for y in range(x, len(s), 3)] for x in range(3)]

out = ""
for x, y, z in zip(blocks[0], blocks[1], blocks[2]):
    out += x + y + z
print(out)
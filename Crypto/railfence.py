import itertools



_in = "Ta _7N6D8Dhlg:W3D_H3C31N__387ef sHR053F38N43DFD i33___N6"

words = _in.split(" ")[::-1]
w = itertools.permutations(words, r = 4)
rails = len(words)

_in = _in


front = True
ptr = 0
word = 0

out = ""
ct = 0
while True:
    try:
        out += words[word][ptr]


    except:
        ct += 1
        if ct == 4:
            break
        pass
    if front:
        word += 1
        if word == 4:
            word = 3
            front = False
            ptr += 1
    else:
        word -= 1
        if word == -1:
            word = 0
            front = True
            ptr += 1

print(out)




print(out)
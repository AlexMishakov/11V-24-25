def R(n):
    bn_n = bin(n)[2:]
    for _ in range(3):
        count_0 = bn_n.count("0")
        count_1 = bn_n.count("1")
        if count_0 == count_1:
            bn_n += bn_n[-1]
        else:
            if count_0 > count_1:
                bn_n += "1"
            else:
                bn_n += "0"
    return int(bn_n, 2)

for n in range(105, 500):
    r = R(n)
    if r % 4 == 0:
        print(n)
        break
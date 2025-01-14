def R(n):
    bn_n = bin(n)[2:]
    c = bn_n.count("1")
    bn_n = bn_n + str(c % 2)
    c = bn_n.count("1")
    bn_n = bn_n + str(c % 2)
    return int(bn_n, 2)

for n in range(500):
    r = R(n)
    if r > 170:
        print(n)
        break
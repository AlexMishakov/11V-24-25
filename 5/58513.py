def R(n):
    bn_n = bin(n)[2:]
    if n % 5 == 0:
        bn_n += bin(5)[2:]
        # bn_n += "101"
    else:
        bn_n += "1"
    if int(bn_n, 2) % 7 == 0:
        bn_n += bin(7)[2:]
        # bn_n += "111"
    else:
        bn_n += "1"
    return int(bn_n, 2)

for n in range(1_000_000, 0, -1):
    r = R(n)
    if r < 1_855_663:
        print(n)
        break

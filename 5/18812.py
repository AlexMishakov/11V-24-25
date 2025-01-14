def R(n):
    n = bin(n)[2:]
    if n.count("1") % 2 == 0:
        n = n + "1"
    else:
        n = n + "0"
    if n.count("1") % 2 == 0:
        n = n + "1"
    else:
        n = n + "0"
    return int(n, 2)


for n in range(100):
    r = R(n)
    if r > 54:
        print(r)
        break
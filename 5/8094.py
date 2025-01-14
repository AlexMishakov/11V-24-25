def R(n):
    n = bin(n)[2:]
    n = n + str(n.count("1") % 2)
    n = n + str(n.count("1") % 2)
    return int(n, 2)

for n in range(100):
    r = R(n)
    if r > 43:
        print(r)
        break

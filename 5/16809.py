def R(n):
    old_n = n
    n = bin(n)[2:]
    c = 8 - len(n)
    n = "0" * c + n
    n = n.replace("1", "*")
    n = n.replace("0", "1")
    n = n.replace("*", "0")
    return int(n, 2) - old_n

for n in range(100):
    r = R(n)
    if r == 133:
        print(n)
        break
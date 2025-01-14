def R(n):
    x = bin(n)[2:]

    ne_chet = ""
    chet = ""

    for i in range(0, len(x), 2):
        ne_chet += x[i]

    for i in range(1, len(x), 2):
        chet += x[i]

    # print(chet, ne_chet)
    one = chet.count("1")
    zero = ne_chet.count("0")
    return abs(one - zero)

for n in range(5000):
    r = R(n)
    # print(r)
    if r == 5:
        print(n)
        break
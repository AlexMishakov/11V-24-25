def R(n):
    a = str(n)
    a1 = int(a[0]) + int(a[1])
    a2 = int(a[2]) + int(a[3])
    if a1 > a2:
        a = str(a2) + str(a1)
    else:
        a = str(a1) + str(a2)
    return a

# print(R(2366))

for n in range(9999, 999, -1):
    if R(n) == "117":
        print(n)
        break

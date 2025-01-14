def f(n, cc):
    out = ""
    while n != 0:
        out = str(n % cc) + out
        n = n // cc
    return out


# for x in range(2030, 0, -1):
#     s = 3**100 - x
#     if f(s, 3).count("0") == 5:
#         print(x)
#         break

print(f(3**3, 3))
print(f(3**10, 3))
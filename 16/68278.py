from functools import lru_cache


@lru_cache()
def F(n):
    if n == 0:
        return 0
    if n % 2 == 0:
        return 4 * F(n / 2)
    else:
        return F(n - 1) + 2 * n - 1

mx = 0
m = []
for a in range(2000):
    for b in range(2000):
        if F(a) - F(b) == 1045:
            mx = max(mx, a - b)
            m.append(a - b)
print(mx, max(m))
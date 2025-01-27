from functools import lru_cache


@lru_cache()
def F(n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return F(n // 100)
    else:
        return (n % 10) * F(n //100)


count = 0
for k in range(10**7, 9 * 10 ** 7 + 1):
    if F(k) == 25:
        count += 1
print(count)

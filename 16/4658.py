def F(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    return F(n-1) * n - 2 * F(n-2)

print(F(6))
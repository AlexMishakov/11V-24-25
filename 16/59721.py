# from functools import lru_cache
# @lru_cache()
import sys

sys.setrecursionlimit(5000)


def F(n):
    if n == 1:
        return n
    return n - 1 + F(n - 1)

print(F(2024) - F(2022))

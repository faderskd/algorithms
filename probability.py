import math
import functools


def k_heads_from_n_coins(n, k):
    n_cached = functools.reduce(lambda a, b: a * b, ((k + i) for i in range(1, n - k + 1))) if n > k else 1
    k_cached = math.factorial(n - k)

    result = n_cached / k_cached
    j = 0
    for i in range(k + 1, n + 1):
        n_cached /= i
        k_cached /= (n - k - j)
        result += n_cached / k_cached
        j += 1

    return result / 2 ** n

print(k_heads_from_n_coins(19, 18))
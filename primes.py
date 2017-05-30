def is_excellent(n):
    i = 2
    s = 1
    while i * i <= n:
        if n % i == 0:
            s += i
            s += n / i
        i += 1

    if i * i == n:
        s -= i
    return s == n and n != 1



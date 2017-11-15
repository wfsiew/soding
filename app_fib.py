def fib(n):
    v = 0
    a, b = 1, 2
    while a < n:
        if a % 2 == 0:
            v += a

        a, b = b, a + b

    return v

if __name__ == '__main__':
    k = fib(4000000)
    print('Sum =', k)
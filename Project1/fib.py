def calc_fib(n):
    start = [0, 1, 1]
    res = start[1:n]
    while res[-1] <= n:
        res.append(res[-1] + res[-2])
    return res[:-1]


print(calc_fib(500))


def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]

    return helper


def f(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return f(x-1) + f(x-2)


fib = memoize(f)
print(fib(40))
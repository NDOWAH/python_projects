def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]

    return helper

@memoize
def f(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return f(x-1) + f(x-2)

for i in range(2, 20):
    print('For i = %s, the result is %s' %(i,f(i)))

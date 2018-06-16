def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper
def fib(n):
    if n == 0 :
        return 0
    elif n == 1 :
        return 1
    else :
        return n*fib(n-1)

fib = memoize(fib)
print(fib(40))

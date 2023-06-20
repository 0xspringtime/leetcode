def fib(n, memo={}):
    if n <= 1:
        return n
    elif n not in memo:
        memo[n] = fib(n-1) + fib(n-2)
    return memo[n]

#The principle behind memoization is simple: whenever we compute a result, we store it in a data structure (like an array or a dictionary). Later, when the same result is needed again, we simply look it up in our data structure instead of recomputing it. This technique is especially useful when we have overlapping subproblems, which is a key characteristic where dynamic programming shines.


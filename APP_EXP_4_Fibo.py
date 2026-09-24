# apply memoization adn tabulation techniques to to efficiently compute nth fibo num
# using dynamic programming in python

# top down approach (memoization)

def fibonacci(n, memo = {}):
    if n<=1:
        return n
    if n in memo:
        return memo[n]
    memo[n] = fibonacci(n-1, memo) + fibonacci(n-1, memo)
    return memo[n]

n = int(input("enter an integer: "))
print(f"fibonacci number of {n} is", fibonacci(n))

# bottom up approach (tabulation)
def fibonacci(n):
    if n<=1:
        return n
    dp = [0]*(n+1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

n = int(input("enter an integer: "))
print(f"the fibonacci number of {n} is:", fibonacci(n))


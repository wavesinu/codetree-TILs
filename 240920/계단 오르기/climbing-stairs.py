import sys


def count_climb(n):
    if n == 0:
        return 1

    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        dp[i] = 0

        if i >= 2:
            dp[i] += dp[i - 2]
        if i >= 3:
            dp[i] += dp[i - 3]
    return dp[n]


n = int(sys.stdin.readline())
print(count_climb(n))
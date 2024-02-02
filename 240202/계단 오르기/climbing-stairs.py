def countWays(n):
    if n == 0:
        return 1
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    elif n == 3:
        return 1
    
    DP = [0] * (n + 1)
    DP[0], DP[1], DP[2], DP[3] = 1, 0, 1, 1
    
    for i in range(4, n + 1):
        DP[i] = DP[i-2] + DP[i-3]
    
    return DP[n]

# 예시
n = int(input())
print(countWays(n))
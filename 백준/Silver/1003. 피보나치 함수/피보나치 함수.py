T = int(input())

for i in range(T):
    N = int(input())
    if N == 0:
        print(1, 0)
    elif N == 1:
        print(0, 1)
    else:
        dp = [1, 0, 0, 1]
        for i in range(N):
            dp[0], dp[1], dp[2], dp[3] = dp[2], dp[3], dp[0] + dp[2], dp[1] + dp[3]
        print(dp[0], dp[1])


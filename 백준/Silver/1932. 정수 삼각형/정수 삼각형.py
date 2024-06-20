if __name__ == '__main__':
    n = int(input())

    dp = []
    for _ in range(n):
        dp.append(list(map(int, input().split())))

    for i in range(1, n):
        for j in range(0, i + 1):
            if j == 0:
                dp[i][0] += dp[i-1][0]

            elif j == i:
                dp[i][j] += dp[i-1][j-1]

            else:
                dp[i][j] += max(dp[i-1][j-1], dp[i-1][j])

    print(max(dp[-1]))

#
# 7                   i=0, j=0 dp[0][0] = 7
# 3 8                 i=1, max(dp[0][0] + dp[1][0] (j=0), dp[0][0] + dp[1][1](j=1))
# 8 1 0               i=2, max(dp[1][0] + dp[2][0] (j=0), dp[1][0] + dp[2][1] (j=1), dp[1][1] + dp[2][1] (j=1), dp[1][1] + dp[2][2] (j=2))
# 2 7 4 4
# 4 5 2 6 5

if __name__ == '__main__':
    n = int(input())

    dp = [0] * 91
    dp[1] = 1

    if n < 2:
        print(dp[n])

    else:
        for i in range(2, n + 1):
            dp[i] = dp[i - 2] + dp[i - 1]

        print(dp[n])

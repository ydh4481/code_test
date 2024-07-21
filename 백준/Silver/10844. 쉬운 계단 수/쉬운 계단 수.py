if __name__ == '__main__':
    mod = 1000000000

    n = int(input())

    dp = [[0] * 10 for _ in range(n + 1)]

    for digit in range(1, 10):
        dp[1][digit] = 1

    for length in range(2, n + 1):
        for digit in range(10):
            if digit > 0:
                dp[length][digit] += dp[length - 1][digit - 1]

            if digit < 9:
                dp[length][digit] += dp[length - 1][digit + 1]

    print(sum(dp[n]) % mod)

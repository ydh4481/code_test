if __name__ == '__main__':
    n = int(input())

    wine = [0]

    for i in range(1, n + 1):
        wine.append(int(input()))

    if n <= 2:
        print(sum(wine))
    else:
        dp = [0] * (n + 1)

        dp[1] = wine[1]
        dp[2] = wine[1] + wine[2]

        for i in range(3, n + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + wine[i], dp[i - 3] + wine[i - 1] + wine[i])

        print(dp[n])

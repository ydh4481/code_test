if __name__ == '__main__':
    n = int(input())

    time_list = []
    price_list = []
    for _ in range(n):
        t, p = map(int, input().split())
        time_list.append(t)
        price_list.append(p)

    dp = [0 for i in range(n + 1)]

    for i in range(len(time_list) - 1, - 1, - 1):
        if time_list[i] + i > n:
            dp[i] = dp[i + 1]
        else:
            dp[i] = max(dp[i + 1], dp[time_list[i] + i] + price_list[i])

    print(dp[0])

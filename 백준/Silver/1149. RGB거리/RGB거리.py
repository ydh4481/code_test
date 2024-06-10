import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline())

    dp = []
    for _ in range(n):
        # [빨강, 초록, 파랑]
        dp.append(list(map(int, sys.stdin.readline().split())))

    # 1번 집은 2번과 같지 않아야 함.
    # N번 집은 N-1번 집과 같이 않아야 함.
    # i(2 <= i <= N-1)번 집은 i-1, i+1번 집과 같지 않아야 함.
    # -> R, G, B 3가지로 나눠서 계산한다.

    for i in range(1, n):
        dp[i][0] += min(dp[i - 1][1], dp[i - 1][2])  # i가 R일 경우, G, B 중 하나를 선택
        dp[i][1] += min(dp[i - 1][0], dp[i - 1][2])  # i가 G일 경우, R, B 중 하나를 선택
        dp[i][2] += min(dp[i - 1][0], dp[i - 1][1])

    print(min(dp[n - 1][0], dp[n - 1][1], dp[n - 1][2]))

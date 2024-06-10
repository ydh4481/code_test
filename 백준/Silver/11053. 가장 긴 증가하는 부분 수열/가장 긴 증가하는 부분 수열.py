import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline().split()))

    # 1, 2 차이

    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    print(max(dp))

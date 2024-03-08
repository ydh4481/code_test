t = int(input())


def check_year(m, n, x, y):
    while x <= m * n:  # 최대 범위
        if (x - y) % n == 0:  # 나머지로 확인
            return x
        x += m
    return -1


for _ in range(t):
    m, n, x, y = map(int, input().split())
    print(check_year(m, n, x, y))

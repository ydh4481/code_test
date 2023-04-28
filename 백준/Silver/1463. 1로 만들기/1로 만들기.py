n = int(input())
answer = set()


def calculate(x, cnt):
    if answer and cnt >= min(answer):
        return 0
    if x == 1:
        answer.add(cnt)
        return 0

    if x % 3 == 0:
        calculate(x // 3, cnt + 1)
    if x % 2 == 0:
        calculate(x // 2, cnt + 1)
    if x % 3 != 0 or x % 2 != 0:
        calculate(x - 1, cnt + 1)


calculate(n, 0)

print(min(answer))

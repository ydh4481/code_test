import math

n = int(input())

if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    cnt = 0
    for two in range(0, n // 2 + 1):
        one = n - 2 * two
        cnt += math.factorial(one + two) // (math.factorial(one) * math.factorial(two))
    print(int(cnt % 10007))

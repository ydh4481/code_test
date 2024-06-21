import math

if __name__ == '__main__':
    t = int(input())
    for test_case in range(t):
        n, m = map(int, input().split())

        print(math.factorial(m) // (math.factorial(m - n) * math.factorial(n)))
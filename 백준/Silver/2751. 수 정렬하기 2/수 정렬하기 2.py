import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())

    numbers = []
    for _ in range(n):
        numbers.append(int(input()))

    for num in sorted(numbers):
        print(num)

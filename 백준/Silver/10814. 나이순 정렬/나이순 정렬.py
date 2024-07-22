import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())

    mans = [[] for _ in range(201)]

    for _ in range(n):
        age, name = input().split()
        mans[int(age)].append(name)

    for age, man in enumerate(mans):
        if man:
            for n in man:
                print(age, n)

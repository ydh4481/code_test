if __name__ == '__main__':
    n = int(input())

    target = 666

    while n:
        if '666' in str(target):
            n -= 1
        target += 1

    print(target - 1)

if __name__ == '__main__':
    n = int(input())

    numbers = [0] * 10000
    for _ in range(n):
        numbers[int(input()) - 1] += 1

    for i in range(10000):
        if numbers[i] != 0:
            for _ in range(numbers[i]):
                print(i + 1)

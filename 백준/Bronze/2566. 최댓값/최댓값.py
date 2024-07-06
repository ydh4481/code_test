if __name__ == '__main__':
    max_answer = -1
    x, y = -1, -1
    for row in range(9):
        numbers = list(map(int, input().split()))
        max_n = max(numbers)
        if max_answer < max_n:
            max_answer = max_n
            x = row
            y = numbers.index(max_n)

    print(max_answer)
    print(x + 1, y + 1)

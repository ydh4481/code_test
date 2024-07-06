if __name__ == '__main__':
    n, m = map(int, input().split())

    matrix_a = []
    matrix_b = []

    for _ in range(n):
        matrix_a.append(list(map(int, input().split())))
    for _ in range(n):
        matrix_b.append(list(map(int, input().split())))

    for a, b in zip(matrix_a, matrix_b):
        result = [str(x + y) for x, y in zip(a, b)]
        print(' '.join(result))

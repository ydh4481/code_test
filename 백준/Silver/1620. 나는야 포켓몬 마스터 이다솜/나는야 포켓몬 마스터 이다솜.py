if __name__ == '__main__':
    n, m = map(int, input().split())

    book = {}
    for _ in range(n):
        poket = input()
        book[str(_ + 1)] = poket
        book[poket] = str(_ + 1)

    for _ in range(m):
        q = input()
        print(book[q])


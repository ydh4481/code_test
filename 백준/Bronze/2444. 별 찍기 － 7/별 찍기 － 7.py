if __name__ == '__main__':
    n = int(input())

    line_cnt = 2 * n - 1

    for i in range(1, n):
        star_cnt = 2 * i - 1
        space_cnt = (line_cnt - star_cnt) // 2
        print(" " * space_cnt + "*" * star_cnt)

    print('*' * line_cnt)

    for i in range(n - 1, 0, -1):
        star_cnt = 2 * i - 1
        space_cnt = (line_cnt - star_cnt) // 2
        print(" " * space_cnt + "*" * star_cnt)

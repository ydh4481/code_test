if __name__ == '__main__':
    n = list(map(int, list(input())))

    if 0 not in n:
        print(-1)

    # 30의 배수
    # 3의 배수가 되기 위해선 각 자리수의 합이 3의 배수이면 3의 배수
    # 10은 뒤에 0이 있어야 10의 배수
    else:
        if sum(n) % 3 != 0:
            print(-1)
        else:
            print(''.join(str(_) for _ in sorted(n, reverse=True)))

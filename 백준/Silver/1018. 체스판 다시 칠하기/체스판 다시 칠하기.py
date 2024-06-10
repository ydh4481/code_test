import sys

if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())

    board = []
    for _ in range(n):
        board.append(list(sys.stdin.readline()))

    color = [
        ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
        ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']
    ]
    min_cnt = 64
    for x in range(0, n - 7):
        for y in range(0, m - 7):
            temp_w_cnt = 0
            temp_b_cnt = 0
            for row in range(8):
                if row % 2 == 0:  # 짝수
                    w_start = sum([1 if color[0][i] != v else 0 for i, v in enumerate(board[row + x][y:y + 8])])
                    b_start = sum([1 if color[1][i] != v else 0 for i, v in enumerate(board[row + x][y:y + 8])])
                else:  # 홀수
                    w_start = sum([1 if color[1][i] != v else 0 for i, v in enumerate(board[row + x][y:y + 8])])
                    b_start = sum([1 if color[0][i] != v else 0 for i, v in enumerate(board[row + x][y:y + 8])])
                temp_w_cnt += w_start
                temp_b_cnt += b_start

            min_cnt = min(min_cnt, min(temp_w_cnt, temp_b_cnt))
    print(min_cnt)

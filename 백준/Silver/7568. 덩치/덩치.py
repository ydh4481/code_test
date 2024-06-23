# 만일 자신보다 더 큰 덩치의 사람이 k명이라면 그 사람의 덩치 등수는 k+1이 된다.

# 2 ≤ N ≤ 50
# 10 ≤ x, y ≤ 200

# input
# 5
# 55 185
# 58 183
# 88 186
# 60 175
# 46 155

# output
# 2 2 1 2 5

if __name__ == '__main__':
    n = int(input())

    mans = []
    for _ in range(n):
        mans.append(list(map(int, input().split())))

    answer = []
    for w, h in mans:
        k = sum([1 for w_, h_ in mans if w_ > w and h_ > h])
        answer.append(str(k + 1))

    print(' '.join(answer))

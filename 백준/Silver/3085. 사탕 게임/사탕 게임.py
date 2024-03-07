n = int(input())


def count_line(line):
    result = [1]
    m = 1
    for i in range(0, len(line) - 1):
        if line[i] == line[i + 1]:
            m += 1
        else:
            m = 1
        result.append(m)
    return max(result)


def check_candy(candies: list, max_candy):
    for i, x in enumerate(candies):
        max_candy = max(count_line(x), max_candy)
        if max_candy == n:
            return max_candy

        y = [_[i] for _ in candies]
        max_candy = max(count_line(y), max_candy)
        if max_candy == n:
            return max_candy

    return max_candy


candies = []
for _ in range(n):
    candies.append([c for c in input()])
max_candy = 0
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
for i in range(n):
    for j in range(n):
        for di, dj in directions:
            i_ = i + di
            j_ = j + dj
            if 0 <= i_ < n and 0 <= j_ < n:
                if candies[i][j] == candies[i_][j_]:
                    continue

                candies[i][j], candies[i_][j_] = candies[i_][j_], candies[i][j]
                if di == 0 or dj == 0:
                    max_candy = check_candy(candies, max_candy)
                if max_candy == n:
                    break
                candies[i][j], candies[i_][j_] = candies[i_][j_], candies[i][j]

print(max_candy)

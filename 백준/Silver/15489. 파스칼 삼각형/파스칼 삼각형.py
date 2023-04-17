R, C, W = [int(_) for _ in input().split()]
# R, C, W = 1, 1, 1
# print(R, C, W)
# 1   2     3       4         5
# 0   1 2   3 4 5   6 7 8 9   10 11 12 13 14
if R + C + W == 3:
    print(3)
else:
    t = []
    for i in range(R + W - 1):
        if i == 0:
            t.append([1])
            continue
        elif i == 1:
            t.append([1, 1])
            continue
        elif i == 2:
            t.append([1, 2, 1])
            continue
        tmp = [1]
        for j in range(1, i):
            tmp.append(t[i - 1][j - 1] + t[i - 1][j])
        tmp.append(1)
        t.append(tmp)
    
    s = 0
    k = C - 1
    for i in range(R - 1, R + W - 1):
        for j in range(k, C):
            s += t[i][j]
            # print(t[i][j], end=' ')
        # print()
        C += 1
    print(s)
    # print(t)
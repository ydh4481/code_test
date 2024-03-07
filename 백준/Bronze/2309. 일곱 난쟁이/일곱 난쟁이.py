from itertools import combinations

mans = []
for i in range(9):
    mans.append(int(input()))

mans = sorted(mans)

for l in combinations(mans, 7):
    if sum(l) == 100:
        for _ in l:
            print(_)
        break

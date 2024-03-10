n, m = list(map(int, input().split()))

# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
# 고른 수열은 오름차순이어야 한다.

from itertools import combinations
for comb in combinations([i for i in range(1, n + 1)], m):
    for _ in comb:
        print(_, end=' ')
    print()

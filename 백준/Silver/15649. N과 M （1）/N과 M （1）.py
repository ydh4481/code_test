n, m = list(map(int, input().split()))

# 1부터 n까지 자연수 중에서 중복 없이 m개를 고른 수열

from itertools import permutations
for perm in permutations([i for i in range(1, n + 1)], m):
    for _ in perm:
        print(_, end=' ')
    print()

n, m = list(map(int, input().split()))

# 1부터 N까지 자연수 중에서 M개를 고른 수열
# 같은 수를 여러 번 골라도 된다.

from itertools import product
for comb in product([i for i in range(1, n + 1)], repeat=m):
    for _ in comb:
        print(_, end=' ')
    print()

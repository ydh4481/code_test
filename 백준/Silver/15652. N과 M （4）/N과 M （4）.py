n, m = list(map(int, input().split()))

# 1부터 N까지 자연수 중에서 M개를 고른 수열
# 같은 수를 여러 번 골라도 된다.
# 고른 수열은 비내림차순이어야 한다.
# 길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다.

from itertools import combinations_with_replacement
for comb in combinations_with_replacement([i for i in range(1, n + 1)], m):
    for _ in comb:
        print(_, end=' ')
    print()

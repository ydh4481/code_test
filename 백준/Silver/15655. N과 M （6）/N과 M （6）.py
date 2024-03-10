n, m = list(map(int, input().split()))
numbers = list(map(int, input().split()))
# N개의 자연수 중에서 M개를 고른 수열
# 고른 수열은 오름차순이어야 한다.
# 한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다.
# 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.



from itertools import combinations
for comb in combinations(sorted(numbers), m):
    for _ in comb:
        print(_, end=' ')
    print()

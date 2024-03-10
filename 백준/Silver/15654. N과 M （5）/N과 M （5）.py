n, m = list(map(int, input().split()))
numbers = list(map(int, input().split()))
# N개의 자연수 중에서 M개를 고른 수열


from itertools import permutations
for perm in permutations(sorted(numbers), m):
    for _ in perm:
        print(_, end=' ')
    print()

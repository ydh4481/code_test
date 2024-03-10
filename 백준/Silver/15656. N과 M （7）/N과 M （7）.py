n, m = list(map(int, input().split()))
numbers = list(map(int, input().split()))

# N개의 자연수 중에서 M개를 고른 수열
# 같은 수를 여러 번 골라도 된다.
# 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.


from itertools import product

for prod in product(sorted(numbers), repeat=m):
    for _ in prod:
        print(_, end=' ')
    print()

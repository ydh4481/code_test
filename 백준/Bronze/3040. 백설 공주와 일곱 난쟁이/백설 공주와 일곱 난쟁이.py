import sys
from itertools import combinations

if __name__ == '__main__':
    # 난쟁이 모자 숫자의 합이 100
    numbers = []
    for _ in range(9):
        numbers.append(int(sys.stdin.readline()))

    comb = []
    for comb in combinations(numbers, 7):
        if sum(comb) == 100:
            for num in comb:
                print(num)
            break



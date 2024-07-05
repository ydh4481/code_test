from itertools import permutations

if __name__ == '__main__':
    n = int(input())
    numbers = list(map(int, input().split()))
    operators = []
    operator_dict = {
        0: '+',
        1: '-',
        2: '*',
        3: '/'
    }
    for idx, cnt in enumerate(map(int, input().split())):
        for _ in range(cnt):
            operators.append(operator_dict[idx])
    max_answer = -1000000000
    min_answer = 1000000000
    for combi in permutations(operators, n - 1):
        # print(combi)
        result = numbers[0]
        # print(result, end=' ')
        for op, n in zip(combi, numbers[1:]):
            # print(op, n, end=' ')
            if op == "+":
                result += n
            elif op == "-":
                result -= n
            elif op == "*":
                result *= n
            else:
                if result < 0:
                    result = abs(result) // n * -1
                else:
                    result //= n
        # print()
        # print(result)
        max_answer = max(max_answer, result)
        min_answer = min(min_answer, result)

    print(max_answer)
    print(min_answer)




# from itertools import permutations
#
# if __name__ == '__main__':
#     n = int(input())
#     numbers = list(map(int, input().split()))
#     operators = []
#     operator_dict = {
#         0: '+',
#         1: '-',
#         2: '*',
#         3: '/'
#     }
#     for idx, cnt in enumerate(map(int, input().split())):
#         for _ in range(cnt):
#             operators.append(operator_dict[idx])
#     max_answer = -1000000000
#     min_answer = 1000000000
#     for combi in permutations(operators, n - 1):
#         # print(combi)
#         result = numbers[0]
#         # print(result, end=' ')
#         for op, n in zip(combi, numbers[1:]):
#             # print(op, n, end=' ')
#             if op == "+":
#                 result += n
#             elif op == "-":
#                 result -= n
#             elif op == "*":
#                 result *= n
#             else:
#                 if result < 0:
#                     result = abs(result) // n * -1
#                 else:
#                     result //= n
#         # print()
#         # print(result)
#         max_answer = max(max_answer, result)
#         min_answer = min(min_answer, result)
#
#     print(max_answer)
#     print(min_answer)

def dfs(idx, total, plus, minus, multiply, divide):
    global max_answer, min_answer

    if idx == n:
        max_answer = max(max_answer, total)
        min_answer = min(min_answer, total)
        return

    if plus > 0:
        dfs(idx + 1, total + numbers[idx], plus - 1, minus, multiply, divide)
    if minus > 0:
        dfs(idx + 1, total - numbers[idx], plus, minus - 1, multiply, divide)
    if multiply > 0:
        dfs(idx + 1, total * numbers[idx], plus, minus, multiply - 1, divide)
    if divide > 0:
        dfs(idx + 1, int(total / numbers[idx]), plus, minus, multiply, divide - 1)


if __name__ == '__main__':
    n = int(input())
    numbers = list(map(int, input().split()))
    operators = list(map(int, input().split()))

    max_answer = -1e10
    min_answer = 1e10

    dfs(1, numbers[0], operators[0], operators[1], operators[2], operators[3])

    print(max_answer)
    print(min_answer)

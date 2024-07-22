import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())

    stack = []
    operators = []
    check = True
    num = 1
    for i in range(n):
        target = int(input())

        while num <= target:
            stack.append(num)
            operators.append('+')
            num += 1

        if stack[-1] == target:
            stack.pop()
            operators.append('-')
        else:
            check = False
            break


    if check:
        for _ in operators:
            print(_)
    else:
        print('NO')

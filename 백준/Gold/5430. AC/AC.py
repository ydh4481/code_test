import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    t = int(input())

    for test_case_id in range(t):
        p = input()
        n = int(input())
        numbers = input()[1:-2]

        if n:
            numbers = list(map(int, numbers.split(',')))
        else:
            numbers = []

        check = True
        reverse_flag = 0
        for func in p:
            if func == 'R':
                reverse_flag += 1
            elif func == 'D':
                if not numbers:
                    check = False
                    break
                if reverse_flag % 2 == 0:
                    numbers.pop(0)
                else:
                    numbers.pop()

        if check:
            if reverse_flag % 2 != 0:
                numbers = numbers[::-1]
            print(str(numbers).replace(' ', ''))
        else:
            print('error')

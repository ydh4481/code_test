import sys

if __name__ == '__main__':
    t = int(sys.stdin.readline())

    for _ in range(t):
        test_data = list(sys.stdin.readline()[:-1])
        stack = []
        answer = 'YES'
        for data in test_data:
            if data == '(':
                stack.append(data)

            else:
                if stack:
                    stack.pop()
                else:
                    answer = 'NO'
                    break
        if stack:
            answer = 'NO'
        
        print(answer)
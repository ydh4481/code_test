t = int(input())
for _ in range(t):
    m = int(input())
    dic = {key: True for key in input().split()}
    n = int(input())
    answers = input().split()
    for answer in answers:
        if dic.get(answer):
            print(1)
        else:
            print(0)
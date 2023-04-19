a = sorted(list(set(_ for _ in range(1, 31)) - set(int(input()) for _ in range(28))))

for _ in a:
    print(_)
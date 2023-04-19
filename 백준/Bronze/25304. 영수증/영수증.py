money = int(input())
n = int(input())

s = 0
for _ in range(n):
    val, num = map(int, input().split())
    s += val * num

if s == money: print('Yes')
else: print('No')
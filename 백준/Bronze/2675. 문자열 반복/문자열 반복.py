num = int(input())
it = []
text = []
ans = []
for i in range(0, num):
    x, y = input().split()
    it.append(int(x))
    text.append(y)
for i in range(num):
    a = ''
    for j in range(len(text[i])):
        a += it[i]*text[i][j]
    ans.append(a)
    
for i in range(num):
    print(ans[i])
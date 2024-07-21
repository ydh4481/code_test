text = input()
alpha =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s',
        't','u','v','w','x','y','z']
ans = []
for i in range(0, len(alpha)):
    if (alpha[i] in text):
        ans.append(text.find(alpha[i]))
    else:
        ans.append(-1)
for i in range(0,len(ans)):
    print(ans[i], end=' ')
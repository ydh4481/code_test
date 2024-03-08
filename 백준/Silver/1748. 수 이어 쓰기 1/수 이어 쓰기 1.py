n = int(input())

one = 1
nine = 9
answer = 0
while True:
    if n > nine:
        answer += len(str(nine)) * 9 * one
        nine = int(str(nine) + '9')
        one *= 10
    else:
        answer += (n - one + 1) * len(str(n))
        break
print(answer)

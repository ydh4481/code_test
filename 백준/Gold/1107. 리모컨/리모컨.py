n = int(input())
m = int(input())

answer = abs(n - 100)
remove_buttons = list(map(int, input().split())) if m else []

for number in range(1000001):
    for num in str(number):
        if int(num) in remove_buttons:
            break
    else:
        answer = min(answer, len(str(number)) + abs(number - n))

print(answer)


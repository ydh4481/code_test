# 처음 5자리에 들어가는 5개의 숫자를 각각 제곱한 수의 합을 10으로 나눈 나머지

numbers = list(map(int, input().split()))
result = 0
for number in numbers:
    result += number ** 2

print(result % 10)
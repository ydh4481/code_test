s = input()
t = [_ for _ in input()]

st = []
for value in s:
    st += value
    while st[-len(t):] == t and len(st) >= len(t):
        del st[-len(t):]


if st:
    print("".join(st))
else:
    print('FRULA')
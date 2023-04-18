import sys

n = int(sys.stdin.readline())

vals = [0.] * n
for i in range(n):
    vals[i] = float(sys.stdin.readline())

m = max(vals)
for i in range(0, n):
    if not vals[i]:
        continue
    tmp = vals[i]
    for j in range(i + 1, n):
        if not vals[j]:
            break
        tmp *= vals[j]
        if tmp > m: m = tmp

print("{:.3f}".format(m))

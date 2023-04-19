n, m = map(int, input().split())

bucket = [0] * n
for _ in range(m):
    i, j, k = map(int, input().split())
    bucket[i-1:j] = [k] * (j - i + 1)

print(' '.join([str(_) for _ in bucket]))

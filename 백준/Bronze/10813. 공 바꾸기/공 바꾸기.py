n, m = map(int, input().split())

bucket = [str(_ + 1) for _ in range(n)]

for _ in range(m):
    i, j = map(int, input().split())
    bucket[i-1], bucket[j-1] = bucket[j-1], bucket[i-1]


print(' '.join(bucket))
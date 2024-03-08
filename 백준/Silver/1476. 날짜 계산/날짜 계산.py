e, s, m = map(int, input().split())


def add_year(e, s, m):
    return e % 15 + 1, s % 28 + 1, m % 19 + 1


year = 1
e_, s_, m_ = 1, 1, 1
while True:
    if e_ != e:
        e_, s_, m_ = add_year(e_, s_, m_)
        year += 1
        continue
    elif s_ != s:
        e_, s_, m_ = add_year(e_, s_, m_)
        year += 1
        continue
    elif m_ != m:
        e_, s_, m_ = add_year(e_, s_, m_)
        year += 1
        continue

    break

print(year)

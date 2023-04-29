from collections import defaultdict

N = int(input())

name = input()
l = len(name)


def is_vaild(dic):
    check = False
    for first in dic[name[0]]:
        for last in dic[name[-1]]:
            if last < first or last - first <= len(name[1:-1]): continue
            distance = (last - first) / (l - 1)
            if distance.is_integer():
                for mid_idx, val in enumerate(name[1:-1]):
                    if first + ((mid_idx + 1) * distance) not in dic[val]:
                        check = False
                        break
                    check = True
            if check: return check
    return check


count = 0
for _ in range(N):
    old_name = input()
    if name in old_name:
        count += 1
        continue

    if len(old_name) < len(name):
        continue

    for i in name:
        if i not in old_name: continue

    dic = defaultdict(list)
    for idx, val in enumerate(old_name):
        dic[val].append(idx)

    if is_vaild(dic): count += 1

print(count)

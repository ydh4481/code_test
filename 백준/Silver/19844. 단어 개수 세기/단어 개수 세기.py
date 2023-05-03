import re

line = input().replace('-', ' ')

r = re.compile("^(c|j|n|m|t|s|l|d|qu)'[a|e|i|o|u|h]")
cnt = 0
for word in line.split():
    if r.search(word): cnt += 2
    else: cnt += 1
    
print(cnt)
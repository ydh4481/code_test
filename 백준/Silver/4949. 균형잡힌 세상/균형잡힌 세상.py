import re
import sys


def is_balance(line):
    target = "[\[|\]|\(|\)]"
    targets = re.findall(target, line)

    if len(targets) % 2 != 0:
        return 'no'
    else:
        stack = []
        for _ in targets:
            if _ in ['(', '[']:
                stack.append(_)
            else:
                if stack:
                    if (_ == ')' and stack[-1] == '(') or (_ == ']' and stack[-1] == '['):
                        stack.pop(-1)
                    else:
                        return 'no'
                else:
                    return 'no'
        if stack:
            return 'no'
        return 'yes'


for line in sys.stdin:
    if line.rstrip() == '.':
        break
    print(is_balance(line))

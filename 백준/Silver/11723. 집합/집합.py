import sys


class Program:
    def __init__(self):
        self.S = set()

    def add(self, x):
        self.S.add(x)

    def remove(self, x):
        if x in self.S:
            self.S.remove(x)

    def check(self, x):
        if x in self.S:
            print(1)
        else:
            print(0)

    def toggle(self, x):
        if x in self.S:
            self.S.remove(x)
        else:
            self.S.add(x)

    def all(self):
        self.S = set(range(1, 21))

    def empty(self):
        self.S = set()


if __name__ == '__main__':
    m = int(input())
    program = Program()

    for _ in range(m):
        line = sys.stdin.readline().split()
        op = line[0]

        if op not in ('all', 'empty'):
            x = int(line[1])
            getattr(program, op)(x)
        else:
            getattr(program, op)()

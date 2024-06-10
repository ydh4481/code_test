import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    n_list = set(map(int, sys.stdin.readline().split()))
    m = int(sys.stdin.readline())
    m_list = list(map(int, sys.stdin.readline().split()))

    for x in m_list:
        if x in n_list:
            print(1)
        else:
            print(0)

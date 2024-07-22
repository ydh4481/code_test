if __name__ == '__main__':
    l = int(input())
    line = list(input())

    hash_value = 0
    for i, s in enumerate(line):
        hash_value += (ord(s) - 96) * (31 ** i)

    print(hash_value)

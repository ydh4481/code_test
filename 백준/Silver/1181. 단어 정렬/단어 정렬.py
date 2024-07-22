if __name__ == '__main__':
    n = int(input())

    words = [set() for _ in range(51)]

    for _ in range(n):
        word = input()
        words[len(word)].add(word)

    for word in words:
        if word:
            for w in sorted(list(word)):
                print(w)

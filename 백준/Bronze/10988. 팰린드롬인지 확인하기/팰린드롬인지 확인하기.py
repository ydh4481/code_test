if __name__ == '__main__':
    word = input()

    mid = len(word) // 2
    left = word[:mid]

    if len(word) % 2 == 0:
        right = word[mid:][::-1]
    else:
        right = word[mid + 1:][::-1]

    if left == right:
        print(1)
    else:
        print(0)

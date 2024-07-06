if __name__ == '__main__':
    words = []
    max_len = 0
    for _ in range(5):
        word = input()
        max_len = max(max_len, len(word))

        words.append(word.ljust(15))

    result = ''
    for i in range(max_len):
        for j in range(5):
            result += words[j][i]

    print(result.replace(' ', ''))

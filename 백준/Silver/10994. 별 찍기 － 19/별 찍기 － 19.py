n = int(input())

if n == 1:
    print('*')


else:
    for i in range(n - 1):
        print('*' + ' *' * i + ('*' * (4 * (n - i - 1) - 1)) + '* ' * i + '*')
        print('*' + ' *' * i + (' ' * (4 * (n - i - 1) - 1)) + '* ' * i + '*')
    print('* ' * (n - 1) + '*' + ' *' * (n - 1))
    for i in range(n - 2, -1, -1):
        print('*' + ' *' * i + (' ' * (4 * (n - i - 1) - 1)) + '* ' * i + '*')
        print('*' + ' *' * i + ('*' * (4 * (n - i - 1) - 1)) + '* ' * i + '*')
    
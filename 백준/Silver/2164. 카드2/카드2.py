from collections import deque

if __name__ == '__main__':
    n = int(input())

    cards = deque([n for n in range(1, n + 1)])

    while len(cards) > 1:
        cards.popleft()
        cards.append(cards.popleft())

    print(cards[0])

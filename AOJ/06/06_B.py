trump = [(s, n) for s in ['S', 'H', 'C', 'D'] for n in range(1, 14)]

n = int(input())
cards = []
for i in range(n):
    suit, num = input().split()
    num = int(num)
    cards.append((suit, num))
for card in trump:
    if card not in set(cards):
        print(*card)

for i in range(1, 3001):
    x, y = input().split()
    x = int(x)
    y = int(y)
    if x == y == 0:
        break
    if x >= y:
        print(y, x)
    else:
        print(x, y)

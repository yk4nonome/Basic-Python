while True:
    n, x = map(int, input().split())
    if n == 0 and x == 0:
        break
    conbination = 0
    for i in range(1, n-1):
        for j in range(i+1, n):
            if j < x - i - j <= n:
                conbination += 1
    print(conbination)

W, H, x, y, r = input().split()
W = int(W)
H = int(H)
x = int(x)
y = int(y)
r = int(r)
if x >= r and y >= r and W >= r + x and H >= r+y:
    print('Yes')
else:
    print('No')

a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
sum = 0
for i in range(a, b + 1):
    if c % i == 0:
        sum += 1
print(sum)

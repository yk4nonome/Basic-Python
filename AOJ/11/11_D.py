n = int(input())
dice1 = list(map(int, input().split()))
x = 1
same = False

while True:
    if x == n:
        break
    dice2 = list(map(int, input().split()))
    for i in range(4):
        dice2[4], dice2[0], dice2[5], dice2[1] = dice2[0], dice2[1], dice2[4], dice2[5]
        for j in range(4):
            dice2[3], dice2[0], dice2[5], dice2[2] = dice2[0], dice2[2], dice2[3], dice2[5]
            for k in range(4):
                dice2[3], dice2[1], dice2[4], dice2[2] = dice2[1], dice2[2], dice2[3], dice2[4]
                if dice2 == dice1:
                    same = True
                    break
    x += 1
if same:
    print("No")
else:
    print("Yes")

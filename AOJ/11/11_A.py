dice = list(map(int, input().split()))
direction = input()
for d in range(len(direction)):
    if direction[d] == "N":
        dice[0], dice[1], dice[5], dice[4] = dice[1], dice[5], dice[4], dice[0]
    elif direction[d] == "S":
        dice[0], dice[4], dice[5], dice[1] = dice[4], dice[5], dice[1], dice[0]
    elif direction[d] == "E":
        dice[0], dice[3], dice[5], dice[2] = dice[3], dice[5], dice[2], dice[0]
    elif direction[d] == "W":
        dice[0], dice[3], dice[5], dice[2] = dice[2], dice[0], dice[3], dice[5]
print(dice[0])

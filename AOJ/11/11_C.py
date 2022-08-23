dice_F = list(map(int, input().split()))
dice = list(map(int, input().split()))
direction = ('CCCCNCCCCNCCCCNCCCCNCNCCCCNNCCCC')
for d in range(len(direction)):
    if direction[d] == "N":
        dice[0], dice[1], dice[5], dice[4] = dice[1], dice[5], dice[4], dice[0]
        if dice_F[0] == dice[0] and dice_F[1] == dice[1] and dice_F[2] == dice[2] and dice_F[3] == dice[3] and dice_F[4] == dice[4]:
            print('Yes')
            break
    elif direction[d] == "C":
        dice[1], dice[3], dice[4], dice[2] = dice[2], dice[1], dice[3], dice[4]
        if dice_F[0] == dice[0] and dice_F[1] == dice[1] and dice_F[2] == dice[2] and dice_F[3] == dice[3] and dice_F[4] == dice[4]:
            print('Yes')
            break
if dice_F[0] != dice[0] or dice_F[1] != dice[1] or dice_F[2] != dice[2] or dice_F[3] != dice[3] or dice_F[4] != dice[4]:
    print('No')

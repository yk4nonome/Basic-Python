while True:
    x = input()
    if x == "0":
        break
    sum = 0
    for n in x:
        sum += int(n)
    print(sum)

while True:
    a, op, b = map(str, input().split())
    a = int(a)
    b = int(b)
    if op == "?":
        break
    elif op == "+":
        print(int(a + b))
    elif op == "-":
        print(int(a - b))
    elif op == "*":
        print(int(a * b))
    elif op == "/":
        print(int(a / b))
    else:
        pass

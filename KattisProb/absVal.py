while True:
    try:
        x = input()

        parts = x.split()

        a = int(parts[0])
        b = int(parts[1])

        print(abs(a-b))
    except EOFError:
        break
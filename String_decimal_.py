for i in range(int(input())):
    n = input()
    for i in n:
        if not i.isdigit():
            print(False)
            break
    else:
        print(True)
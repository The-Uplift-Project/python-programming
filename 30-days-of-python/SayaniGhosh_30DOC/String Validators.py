if __name__ == '__main__':
    st = input()
    c1 = 0
    c2 = 0
    c3 = 0
    c4 = 0
    c5 = 0
    for s in st:
        if (s.isalnum() == 1):
            c1 += 1
        if (s.isalpha() == 1):
            c2 += 1
        if (s.isnumeric() == 1):
            c3 += 1
        if (s.islower() == 1):
            c4 += 1
        if (s.isupper() == 1):
            c5 += 1

    if (c1 > 0):
        print("True")
    else:
        print("False")
    if (c2 > 0):
        print("True")
    else:
        print("False")
    if (c3 > 0):
        print("True")
    else:
        print("False")
    if (c4 > 0):
        print("True")
    else:
        print("False")
    if (c5 > 0):
        print("True")
    else:
        print("False")


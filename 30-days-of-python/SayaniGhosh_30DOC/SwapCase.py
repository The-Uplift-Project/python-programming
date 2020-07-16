def swap_case(s):
    r = ""
    for i in s:
        if (i.islower() == 1):
            r = r + i.upper()
        elif (i.isupper() == 1):
            r = r + i.lower()
        else:
            r = r + i
    return r


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

def split_and_join(line):
    # write your code here
    st = ""
    for i in line:
        if (i == " "):
            st = st + "-"
        else:
            st = st + i
    return st


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

def print_formatted(number):
    # your code goes here

    w = len(str(bin(n))) - 2

    for i in range(1, number + 1):
        s1 = str(oct(i))
        s2 = str(hex(i)).upper()
        s3 = str(bin(i))

        print(str(i).rjust(w) + " " + s1[2:].rjust(w) + " " + s2[2:].rjust(w) + " " + s3[2:].rjust(w))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

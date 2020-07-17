
import textwrap


def wrap(string, max_width):
    s = ""
    c = 0
    for i in range(0, len(string)):
        c += 1
        if (c % max_width == 0):
            s = s + string[i] + "\n"
        else:
            s = s + string[i]

    return s


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

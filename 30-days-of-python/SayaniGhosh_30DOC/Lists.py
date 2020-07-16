if __name__ == '__main__':
    N = int(raw_input())
l = []


def op(st):
    if (st[0] == "insert"):
        l.insert(int(st[1]), int(st[2]))
    if (st[0] == "append"):
        l.append(int(st[1]))
    if (st[0] == "remove"):
        l.remove(int(st[1]))
    if (st[0] == "sort"):
        l.sort()
    if (st[0] == "pop"):
        l.pop()
    if (st[0] == "reverse"):
        l.reverse()
    if (st[0] == "print"):
        print(l)


s = []
for i in range(0, N):
    s = raw_input().split()
    op(s)

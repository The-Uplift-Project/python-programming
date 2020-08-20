# Encoding function for PlayFair Cipher

def Enc(strn, inp):

    # Index returning function
    def iret(ch, k):
        li = []
        for i in range(5):
            for j in range(5):
                if ch == k[i][j]:
                    li.append(i)
                    li.append(j)
                    break
        return li

    # Creating square key
    li = list(inp)
    chars = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    j = 0
    l = []
    lis = []
    lis.extend(li)
    while j != 25:
        ch = chars[j]
        if ch not in li:
            lis.append(ch)
        j += 1
    j = 0
    i = 0
    lu = []
    while j != 25:
        lu.append(lis[j])
        if i == 4:
            l.append(lu)
            i = 0
            lu = []
            j += 1
            continue

        i += 1
        j += 1
    k = l

    # Encrypting the message

    if (len(strn) % 2) != 0:
        strn += "Z"
    m = 0
    for ch in strn:
        if ch == "J":
            strn.replace("I", m)
        m += 1
    li = []
    lis = []
    j = 0
    i = 0
    while j != len(strn):
        li.append(strn[j])
        j += 1
        if i == 1:
            lis.append(li)
            i = 0
            li = []
            continue
        i += 1

    msg = ""

    for c in range(len(lis)):
        x = iret(lis[c][0], k)
        r1 = x[0]
        c1 = x[1]

        y = iret(lis[c][1], k)
        r2 = y[0]
        c2 = y[1]

        if c1 == c2:
            msg = msg + k[(r1 + 1) % 5][c1] + k[(r2 + 1) % 5][c2]
        elif r1 == r2:
            msg = msg + k[r1][(c1 + 1) % 5] + k[r2][(c2 + 1) % 5]
        else:
            msg = msg + k[r1][c2] + k[r2][c1]
    return msg


# Decoding Function for PlayFair Ciphering

def Dec(strn, inp):

    # Index returning function
    def iret(ch, k):
        li = []
        for i in range(5):
            for j in range(5):
                if ch == k[i][j]:
                    li.append(i)
                    li.append(j)
                    break
        return li

    # Creating square key
    li = list(inp)
    chars = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    j = 0
    l = []
    lis = []
    lis.extend(li)
    while j != 25:
        ch = chars[j]
        if ch not in li:
            lis.append(ch)
        j += 1
    j = 0
    i = 0
    lu = []
    while j != 25:
        lu.append(lis[j])
        if i == 4:
            l.append(lu)
            i = 0
            lu = []
            j += 1
            continue

        i += 1
        j += 1

    k = l

    # Decrypting the message
    li = []
    lis = []
    j = 0
    i = 0
    while j != len(strn):
        li.append(strn[j])
        j += 1
        if i == 1:
            lis.append(li)
            i = 0
            li = []
            continue
        i += 1

    msg = ""

    for c in range(len(lis)):
        x = iret(lis[c][0], k)
        r1 = x[0]
        c1 = x[1]

        y = iret(lis[c][1], k)
        r2 = y[0]
        c2 = y[1]

        if c1 == c2:
            msg = msg + k[(r1 - 1) % 5][c1] + k[(r2 - 1) % 5][c2]
        elif r1 == r2:
            msg = msg + k[r1][(c1 - 1) % 5] + k[r2][(c2 - 1) % 5]
        else:
            msg = msg + k[r1][c2] + k[r2][c1]
    if msg[-1] == "Z":
        msg = msg[:-1]

    return msg

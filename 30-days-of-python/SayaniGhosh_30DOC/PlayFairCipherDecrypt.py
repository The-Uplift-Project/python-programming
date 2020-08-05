# Decrypt PlayFair Cipher Messages


# index return
def iret(ch, k):
    li = []
    for i in range(5):
        for j in range(5):
            if ch == k[i][j]:
                li.append(i)
                li.append(j)
                break
    return li


# Decrypting the message using the PlayFair ciphering process
def pf_decrypt(strn, k):
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
            msg = msg + k[(r1 - 1)%5][c1] + k[(r2 - 1)%5][c2]
        elif r1 == r2:
            msg = msg + k[r1][(c1 - 1)%5] + k[r2][(c2 - 1)%5]
        else:
            msg = msg + k[r1][c2] + k[r2][c1]
    if msg[-1] == "z":
        msg = msg[:-1]
    return msg


# Key function to make the key square
def key():
    inp = input("Enter key : ")
    inp = inp.lower()
    li = list(inp)
    chars = "abcdefghiklmnopqrstuvwxyz"
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
    return l


# Execution of the whole Decoding Process
t = ""
while t != "exit":

    print("Enter message to decrypt")
    st = input()
    k = key()

    e_msg = pf_decrypt(st, k)
    print("Original text : "+e_msg)

    print("Want to decrypt again? Press 'c'. Or Press 'exit' to end process.")
    t = input()

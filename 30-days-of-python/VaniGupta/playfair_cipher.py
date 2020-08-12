def key_table(inp):
    key = list(dict.fromkeys(inp))
    k = 0
    x = 65
    a= [[0 for i in range(5)]for i in range(5)]
    for i in range(5):
        for j in range(5):
            if k < len(key):
                a[i][j] = key[k].upper()
                k += 1
            elif not any(chr(x) in y for y in a) and chr(x) != 'J':
                a[i][j] = chr(x)
                x += 1
            else:
                while any(chr(x) in y for y in a) or chr(x) == 'J':
                    x += 1
                a[i][j] = chr(x)
    return a

def converted_chunks(msg):
    lst = msg.split()
    msg_list =  []
    for item in lst:
        msg_list += item

    chunks = []
    i = 0
    while i < len(msg_list):
        if i == len(msg_list)-1:
            chunks.append([msg_list[i].upper(), 'X'])
        elif msg_list[i] != msg_list[i + 1]:
            chunks.append([msg_list[i].upper(), msg_list[i+1].upper()])
            i += 1
        else:
            chunks.append([msg_list[i].upper(), 'X'])
        i += 1
    return chunks


def find_coord(c):
    for i in range(5):
        for j in range(5):
            if a[i][j] == c:
                return i, j


def encrypt(chunks):
    enc = ""
    for item in chunks:
        st = ""
        x1, y1 = find_coord(item[0])
        x2, y2 = find_coord(item[1])
        if y1 == y2:
            enc += a[(x1+1)%5][y1] + a[(x2+1)%5][y1]
        elif x1 == x2:
            enc += a[x1][(y1+1)%5] + a[x2][(y2+1)%5]
        else:
            st += a[x2][y1] + a[x1][y2]
            enc += st[::-1] 
    return enc

def decrypt(chunks):
    dec = ""
    for item in chunks:
        st = ""
        x1, y1 = find_coord(item[0])
        x2, y2 = find_coord(item[1])
        if y1 == y2:
            dec += a[x1-1][y1] + a[x2-1][y1]
        elif x1 == x2:
            dec += a[x1][y1-1] + a[x2][y2-1]
        else:
            dec += a[x1][y2] + a[x2][y1]
    if 'X' in dec:
        dec = dec.replace('X', '')
    return dec


inp = []
inp += input("Enter Key:")
a = key_table(inp)
msg = input("Enter Text:")
flag = 0
if 'j' in msg:
    flag = 1
    msg = msg.replace('j', 'i')
chunks = converted_chunks(msg)
enc = encrypt(chunks)
print("Encrypted Text:{}".format(enc))
dec_chunks = converted_chunks(enc)
dec = decrypt(dec_chunks)
print("Dncrypted Text:{}".format(dec))

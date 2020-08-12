inp = input("Enter string: ")
key = input("Enter key: ")
if len(key) > len(inp):
    key = key[:len(inp)]

elif len(key) < len(inp):
    key = (key * ((len(inp) // len(key)) + 1))[:len(inp)]

def b(inp, key):
    res = ""

    for i in range(len(inp)):

        if inp[i].isupper(): v = 'A'
        else: v = 'a'
        s = ord(key[i]) - ord(inp[i])
        if s < 0: s += 26
        res += chr(s + ord(v))

    return res

print("Encoded: {} and Decoded: {}".format(b(inp,key), b(b(inp,key),key)))

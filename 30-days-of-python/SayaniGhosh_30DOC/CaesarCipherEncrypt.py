# Encrypt Caesar Cipher Messages
def c_encrypt(strn, sft):
    msg = ""
    for i in range(len(strn)):
        ch = strn[i]

        if ch == ' ':
            msg += ch
            continue
        if ch.isupper():
            msg += chr((ord(ch) + sft - 65) % 26 + 65)
        else:
            msg += chr((ord(ch) + sft - 97) % 26 + 97)
    return msg


t = ""
while t != "exit":
    print("Enter message to encrypt")
    st = input()
    print("Enter shift value")
    s = int(input())

    e_msg = c_encrypt(st, s)
    print(e_msg)

    print("Want to encrypt again? Press 'c'. Or Press 'exit' to end process.")
    t = input()

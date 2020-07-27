# Decrypt Caesar Cipher Messages
def c_decrypt(strn, sft):
    msg = ""
    for i in range(len(strn)):
        ch = strn[i]
        if ch.isupper():
            msg += chr((ord(ch) - sft - 65) % 26 + 65)
        else:
            msg += chr((ord(ch) - sft - 97) % 26 + 97)
    return msg


t = ""
while t != "exit":
    print("Enter message to decrypt")
    st = input()
    print("Enter key value")
    s = int(input())

    e_msg = c_decrypt(st, s)
    print(e_msg)

    print("Want to decrypt again? Press 'c' to continue. Or Press 'exit' to end process.")
    t = input()

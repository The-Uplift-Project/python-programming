def enc(s,k):
    e=""
    for letter in s:
        if letter.isupper():
            e+= chr((ord(letter) + k-65) % 26 + 65)
        else:
            e += chr((ord(letter) + k - 97) % 26 + 97)
    return e

def dec(s,k):
    d=""
    for letter in s:
        if letter.isupper():
             d+= chr((ord(letter) + (26-k)-65) % 26 + 65)
        else:
            d+= chr((ord(letter) + (26-k) - 97) % 26 + 97)
    return d

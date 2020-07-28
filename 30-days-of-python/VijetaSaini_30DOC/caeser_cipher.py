import string
import collections


def caesar_cipher(rotate_string,no_to_rotate_by):
    upper = collections.deque(string.ascii_uppercase)
    lower = collections.deque(string.ascii_lowercase)

    upper.rotate(no_to_rotate_by)
    lower.rotate(no_to_rotate_by)

    #making  them list
    upper=''.join(list(upper))
    lower=''.join(list(lower))

    return rotate_string.translate(string.maketrans(string.ascii_uppercase,upper)).translate(string.maketrans(string.ascii_lowercase,lower))

our_string= "You only fail when you stop trying!"
for i in range(len(string.ascii_uppercase)):
    print caesar_cipher(our_string, i)


plaintext="columnar transposition cipher"
key=5   #denotes the number of columns to be taken


ciphertext=['']* key   #declares ciphertext with blank columns and number of columns is equal to the key value

print(ciphertext)
print(len(plaintext))   #to print the length of the plaintext

for column in range(key):
    pointer=column

    while pointer<len(plaintext):           #loop works until the pointer is less than the len(plaintext)
        ciphertext[column]+=plaintext[pointer]            #values are added to the  columns from the plaintext at the pointer position
        print(ciphertext)  #print the ciphertext as a list
        pointer+=key                                         #updates the pointer with key value


print(''.join(ciphertext))  #prints the cipher text as a string


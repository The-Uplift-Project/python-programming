'''
Atbash cipher is a substitution cipher with just one specific key where all the letters are reversed that is A to Z and Z to A.
It was originally used to encode the Hebrew alphabets but it can be modified to encode any alphabet.

Atbash Table = {'A' : 'Z', 'B' : 'Y', 'C' : 'X', 'D' : 'W', 'E' : 'V', 
        'F' : 'U', 'G' : 'T', 'H' : 'S', 'I' : 'R', 'J' : 'Q', 
        'K' : 'P', 'L' : 'O', 'M' : 'N', 'N' : 'M', 'O' : 'L', 
        'P' : 'K', 'Q' : 'J', 'R' : 'I', 'S' : 'H', 'T' : 'G', 
        'U' : 'F', 'V' : 'E', 'W' : 'D', 'X' : 'C', 'Y' : 'B', 'Z' : 'A'}

You may use the following table but here I've used a different approach.
My approach is mostly based on the fact that each character has its own counterpart at the opposite end.
So, what I did was that find the middle point the character set and just calculated the difference to obtain the counterpart.
Like:
A <-------------- M , N --------------> Z
65<--------------77, 78 --------------> 90

Given character be G (71)
So 71-78 gives -7
And 77-(-7) = 77+7 = 84 ,i.e, T
'''

#The funtion to encrypt and decrypt.
def Atbashconvert(string):
    #Initializing the output string.
    result = ''
    #For loop for iterating through each character in given string.
    for c in string:
        #Checks if the character is in Upper case
        if c.isupper():
            #Converting the character to its counterpart.
            result += chr(77 - (ord(c)-78))
            #----------------------------------------------------------------
            #result += chr(155 - ord(c)) <--------------------Shorter
        #Checks if the character is in Lower case.
        elif c.islower():
            #Converting the character to its counterpart.
            result += chr(109 - (ord(c)-110))
            #----------------------------------------------------------------
            #result += chr(219 - ord(c)) <---------------------Shorter
        else:
            #If the character is not an alphabet the we do not alter the character.
            result += c
    #Returning the result.
    return result

'''
#The Driver Code
t = ""
while t != "exit":
    print("Enter the Message:")
    message = input()
    converted = convert(message) #converts the message
    print(converted)
    print("Want to use again? Press 'Yes'. Or Press 'exit' to end process.")
    t = input().lower() # converts the input to lowercase to avoid typos.
'''
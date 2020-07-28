alphabets='abcdefghijklmnopqrstuvwxyz'

string_input=str(input("Enter your text that you want to convert:"))
key=int(input("Enter the key value:"))

soutpt=""
n=len(string_input)

for i in range(n):
    character=string_input[i]
    location=alphabets.find(character)
    new_loc=(location+key)%26
    print("character",character,"location",location,"new location",new_loc)
    soutpt+=alphabets[new_loc]

print(otpt)

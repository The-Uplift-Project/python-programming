from itertools import permutations

#test1= "WORD 4"
#test2= "WORD 2"
#test3= "WORD 1"

def permut(word,r):
    for p in sorted(list(permutations(word,int(r)))):
        print(''.join(p))

if __name__ == '__main__':
    s = input("Enter the word and length of each outcome: ")
    word,r = s.split()
    permut(word,r)


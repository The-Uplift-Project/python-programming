#HackerearthPrasunthedetective
#https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/prasun-the-detective-77f90f8f/

#g=ans
def isAnagram(s,t):
    anagram=[0]*52
    i=0
    j=0
    while(i<len(s) and i<len(t)):
        if ord(s[i]) >=65 and ord(s[i]) <= 90:
            anagram[ord(s[i])-65]+=1
        elif ord(s[i])>=97 and ord(s[i])<=122:
            anagram[ord(s[i])-97]+=1
        if ord(t[i])>=65 and ord(t[i])<=90:
            anagram[ord(t[i])-65]-=1
        elif ord(t[i])>=97 and ord(t[i])<=122:
            anagram[ord(t[i])-97]-=1
        i+=1
    j=i
    while(i<len(s)):
        if ord(s[i])>=65 and ord(s[i])<=90:
            anagram[ord(s[i])-65]+=1
        elif ord(s[i]) >=97 and ord(s[i])<=122:
            anagram[ord(s[i])-97]+=1
        i+=1
    while(j<len(t)):
        if ord(t[j])>=65 and ord(t[j])<=90:
            anagram[ord(t[j])-65]-=1
        elif ord(t[j])>=97 and ord(t[j])<=122:
            anagram[ord(t[j])-97]-=1
        j+=1
    #print(anagram)
    for i in range(len(anagram)):
        if anagram[i]<0 or anagram[i]>0:
            return False
    return True
    
#s=input()
#t=input()
s="jogod #! siara."
t="raja is good!"
if isAnagram(s,t):
    print("YES")
else:
    print("NO")
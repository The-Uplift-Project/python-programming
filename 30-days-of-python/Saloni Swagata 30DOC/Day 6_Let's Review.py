# Enter your code here. Read input from STDIN. Print output to STDOUT
T=int(input("Enter the number of test cases: "))
while(T>0):
    s=input("Enter a word: ")
    es=""
    os=""
    for i in range(len(s)):
        if i%2==0:
            es+=s[i]
        else:
            os+=s[i]
    print(es+" "+os)
    T-=1

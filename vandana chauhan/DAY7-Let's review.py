# Enter your code here. Read input from STDIN. Print output to STDOUT
for i in range(int(input())):
    str1=str(input())
    #to get the pattern simply specify stride while slicing
    print(str1[::2],end=' ')
    print(str1[1::2])
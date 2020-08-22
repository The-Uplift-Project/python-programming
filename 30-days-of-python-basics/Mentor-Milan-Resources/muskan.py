def sayHelloTOMe():
    print("Hello Muskan")
n = 7
def takeNo(n):
    m = (n+1)//2
    generatePattern(1,m+1,1)
    generatePattern(n-m,0,-1)
def generatePattern(a,b,c):
    for i in range(a,b,c):
        #e space
        print(' '*(m-i),end='')#6//2=3-1=2#
        #print '*'
        print('*',end ='')
        #i. space
        print(' '*(2*(i-1)-1),end='')
        #print '*' if not 1st line or last line
        if i!=1:
            print('*',end = '')
        print()

if __name__ == '__main__':
    sayHelloToMe()
    takeNo(n)
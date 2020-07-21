import math
print("\t\t----------------------CALCULATOR--------------------")
def sum(a,b):
    a+=b
    return a
def sub(a,b):
    a-=b
    return a
def mult(a,b):
    a*=b
    return a
def div(a,b):
    q=a/b
    r=a%b
    print("\nthe quotient is : %s" %q)
    print("\nthe remainder is : %s" %r)
def sqr(a):
    c=a*a
    d=math.sqrt(a)
    print("\nsquare is : %s" %c)
    print("\nsquare root is :%s" %d)
while(True):
    print("\n\nChoose the operation you want to perform: ")
    print("\n\t1.ADDITION")
    print("\n\t2.SUBTRACTION")
    print("\n\t3.MULTIPLICATION")
    print("\n\t4.DIVISION")
    print("\n\t5.SQUARE PROPERTIES")
    print("\n\t6.EXIT")
    choice=int(input('>'))


    if choice==1:
        print("\n\nEnter the numbers: ")
        num1=int(input('>'))
        num2=int(input('>'))
        s=sum(num1,num2)
        print("\nThe sum is : %s" %s)
    elif choice==2:
        print("\n\nEnter the numbers: ")
        num1=int(input('>'))
        num2=int(input('>'))
        m=sub(num1,num2)
        print("\nThe difference is : %s" %m)
    elif choice==3:
        print("\n\nEnter the numbers: ")
        num1=int(input('>'))
        num2=int(input('>'))
        p=mult(num1,num2)
        print("\nThe multiplication is : %s" %p)
    elif choice==4:
        print("\n\nEnter the numbers: ")
        num1=int(input('>'))
        num2=int(input('>'))
        div(num1,num2)
    elif choice==5:
        print("\n\nEnter the number: ")
        num=int(input('>'))
        sqr(num)
    else:
        print("\n\nThe choice is not in the scope:|")
        print("\nexit")
        break

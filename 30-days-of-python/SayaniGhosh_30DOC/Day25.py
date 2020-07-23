# Enter your code here. Read input from STDIN. Print output to STDOUT
import math


def check_prime(num):
    if num == 1:
        return "Not prime"
    i = 2
    flag = 0
    n = math.sqrt(num)
    while (i <= n):
        if (num % i == 0):
            return "Not prime"
            flag = 1
            break
        i += 1
    if (flag == 0):
        return "Prime"


t = int(input())
while (t):
    n = int(input())
    print(check_prime(n))
    t -= 1




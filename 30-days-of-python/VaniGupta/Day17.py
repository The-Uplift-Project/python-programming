class Calculator:
    def power(self, n, p):
    
        try:
            if n < 0 or p < 0:
            # if any of them is negative, raise exception explicitly
                raise Exception
            return pow(n,p)
        except:
            return "n and p should be non-negative"

myCalculator=Calculator()
print("Enter input lines: ", end = "")
T=int(input())

for i in range(T):
# enter values of n and p respectively
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)   

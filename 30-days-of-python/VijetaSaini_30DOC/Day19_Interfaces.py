#Day19 Code
#Interfaces

class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        if n==1:
            return 1
        else:
            total_value=n+1
            for i in range(2,n//2+1): 
                if n%i==0:
                    total_value+=i
        return total_value        


n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)

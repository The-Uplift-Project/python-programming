#Day14 Code
#scope


class Difference:
    def __init__(self, a):
        self.__elements = a

    # Add your code here
    
    def computeDifference(self):
       self.maximumDifference=(max(self.__elements)-min(self.__elements))
       return self.maximumDifference

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)

class Difference:
    def __init__(self, a):
        self.__elements = a

    maximumDifference = 0
    def computeDifference(self):
        self.maximumDifference = abs(max(self.__elements) - min(self.__elements))
        # print(self.maxDifference)

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)

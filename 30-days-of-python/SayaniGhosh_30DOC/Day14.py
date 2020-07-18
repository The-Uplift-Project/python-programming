class Difference:
    def __init__(self, a):
        self.__elements = a

    # Add your code here
    def computeDifference(self):
        li = []
        for i in self.__elements:
            for j in self.__elements:
                x = i - j
                if (x < 0):
                    x = (-1) * x
                li.append(x)
        self.maximumDifference = max(li)

    # End of Difference class


_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
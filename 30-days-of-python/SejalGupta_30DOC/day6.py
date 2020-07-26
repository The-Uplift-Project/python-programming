#Plus one

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if (len(digits) == 0):
            return
        num = ''
        for i in digits:
            num += str(i)
        n = int(num) + 1
        d = []
        for j in str(n):
            d.append(int(j))
        return (d)
        
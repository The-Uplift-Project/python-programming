#Hamming distance

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        cnt = 0
        l1 = bin(x)[2:]
        l2 = bin(y)[2:]
        lx = len(l1)
        ly = len(l2)
        if (lx != ly):
            if (lx > ly):
                z = '0' * (lx - ly)
                l2 = z + l2
            else:
                z = '0' * (ly - lx)
                l1 = z + l1
        for i,j in zip(l1, l2):
            if (i != j):
                cnt += 1
        return (cnt)
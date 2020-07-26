#Ugly number

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        res = []
        s = set()
        heapq.heappush(res, 1)
        while (len(res) > 0 and n > 0):
            x = res[0]
            heapq.heappop(res)
            n -= 1
            if (n == 0):
                print (len(res))
                return (x)
            for m in [2, 3, 5]:
                next = m * x
                if next not in s:
                    heapq.heappush(res, next)
                    s.add(next)
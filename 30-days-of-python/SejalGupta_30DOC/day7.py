#Island perimeter

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        l, e = 0, 0
        
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    l += 1
                    if i > 0 and grid[i-1][j] == 1:
                        e += 1
                    if j > 0 and grid[i][j-1] == 1:
                        e += 1
        return (l * 4 - e * 2)
        
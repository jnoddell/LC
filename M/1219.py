class Solution:
    
    def __init__(self):
        self.maximum = float("-inf")

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        
        def traverse(i, j, g, running_sum):
            
            if (i < 0 or j < 0 or i > len(grid) - 1 or j > len(grid[0]) - 1 or g[i][j] == 0):
                return
            
            running_sum += g[i][j]
            g[i][j] = 0
            
            traverse(i-1, j, g, running_sum)
            traverse(i+1, j, g, running_sum)
            traverse(i, j-1, g, running_sum)
            traverse(i, j+1, g, running_sum)
            g[i][j] = grid[i][j]
            
            if running_sum > self.maximum:
                self.maximum = running_sum
        
        for i in range(len(grid)):
            
            for j in range(len(grid[0])):
                
                traverse(i, j, [cell[:] for cell in grid], 0)
        
        return self.maximum

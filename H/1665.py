class Solution:
    
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        
        tasks.sort(key = lambda x: x[1] - x[0], reverse = True)
        
        curr, init = 0, 0
        
        for actual, minimum in tasks:
            
            delta = max(0, minimum - curr)
            
            init += delta
            
            curr += delta - actual
            
        return init

class Solution(object):
    
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        queue = list()
        
        for char in s:
            
            if char in "({[":
                
                queue.append(char)
                
            elif char in ")":
                
                if len(queue) > 0 and queue[-1] in "(":
                    
                    queue.pop()
                    
                else:
                    
                    return False
            
            elif char in "}":
                
                if len(queue) > 0 and queue[-1] in "{":
                    
                    queue.pop()
                    
                else:
                    
                    return False
                
            elif char in "]":
                
                if len(queue) > 0 and queue[-1] in "[":
                    
                    queue.pop()
                    
                else:
                    
                    return False
        
        if len(queue) > 0:
            
            return False
        
        return True

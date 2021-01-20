class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        is_neg = False
        if x < 0:
            is_neg = True
            x = -x
        
        x = str(x)[::-1]
        x = int(x)
        
        if x > 2**31-1:
            return 0
        
        if is_neg:
            x = 0 - x
        
        return x

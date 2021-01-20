class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        running_sum = 0
        result = []
        
        for n in nums:
            result.append(n + running_sum)
            running_sum += n
            
        return result

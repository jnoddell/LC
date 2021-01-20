class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        ret = list()
        
        for i in range(0, n):
            ret.append(nums[i])
            ret.append(nums[n+i])
        
        return ret

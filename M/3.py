class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        substr = []
        curr = []
        
        for i in range(0, len(s)):
            letter = s[i:i+1]
            if letter in curr:
                if len(curr) > len(substr):
                    substr = curr
                index_cut = curr.index(letter)
                curr = curr[index_cut+1:]
            curr.append(letter)
        
        if len(curr) > len(substr):
                    substr = curr
            
        return len(substr)

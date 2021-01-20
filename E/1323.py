class Solution:
    
    def maximum69Number (self, num: int) -> int:
        
        numstr = str(num)
        num_max = num
        index6 = -1
        for i in range(0, len(numstr)):
            digit = numstr[i:i+1]
            if digit in "6":
                index6 = i
                currstr = numstr[:index6] + "9" + numstr[index6+1:]
                curr = int(currstr)
                if curr > num_max:
                    num_max = curr
        
        return num_max

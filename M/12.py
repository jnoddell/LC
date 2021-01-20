class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        exchange = [['I', 1], ['V', 5], ['X', 10], ['L', 50], ['C', 100], ['D', 500], ['M', 1000]]
        exchange = exchange[::-1]
        roman = ""
        
        index = 0
        while num > 0:
            curr_tuple = exchange[index]
            curr_symbol = curr_tuple[0]
            curr_value = curr_tuple[1]
        
            increment_index = True
            
            if num - curr_value == 0:
                return (roman + curr_symbol)
            elif num - curr_value > 0:
                num -= curr_value
                roman += curr_symbol
                increment_index = False
            elif increment_index and num - 900 >= 0:
                num -= 900
                roman += "CM"
            elif index > 0 and increment_index and num - 400 >= 0:
                num -= 400
                roman += "CD"
            elif index > 1 and increment_index and num - 90 >= 0:
                num -= 90
                roman += "XC"
            elif index > 2 and increment_index and num - 40 >= 0:
                num -= 40
                roman += "XL"
            elif index > 3 and increment_index and num - 9 >= 0:
                num -= 9
                roman += "IX"
            elif index > 4 and increment_index and num - 4 >= 0:
                num -= 4
                roman += "IV"
            
            if num == 0:
                return roman
            elif increment_index:
                index += 1

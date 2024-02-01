# 13. Roman to Integer ZROBIONE

class Solution(object):
    def romanToInt(self, s):
    
        dict = {"I": 1,
                "V": 5,
                "X": 10,
                "L": 50,
                "C": 100,
                "D": 500,
                "M": 1000}
        
        s = s.replace("CM", "DCCCC").replace("IX", "VIIII")
        s = s.replace("XC", "LXXXX").replace("XL", "XXXX")
        s = s.replace("IV", "IIII").replace("CD", "CCCC")
        
        sum = 0
        for i in range(len(s)):
            sum = sum + dict[s[i]]
        
        print(sum) # return sum
            
Solution().romanToInt("MCMXCIV") # 1994 <- the proper sum 
# 1929. Concatenation of Array ZROBIONE

class Solution(object):
    def getConcatenation(self, nums):
        for i in range(len(nums)):
            nums.append(nums[i])
            
        return nums
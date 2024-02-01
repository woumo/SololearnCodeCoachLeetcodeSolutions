# 1523. Count Odd Numbers in an Interval Range ZROBIONE

class Solution(object):
    def countOdds(self, low: int, high: int):
        if low % 2 == 0 and high % 2 == 0:
            return (high-low)//2
        else:
            return (high-low)//2 + 1
        
print(Solution().countOdds(3,11))
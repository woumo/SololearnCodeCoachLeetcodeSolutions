# 2413. Smallest Even Multiple  ZROBIONE

class Solution(object):
    def smallestEvenMultiple(self, n):
        
        ans = 0

        if n % 2 == 0:
                ans = n         
        elif n % 2 != 0:
            ans = n*2
        
        
        # return ans
        print(ans)
        
Solution().smallestEvenMultiple(5)
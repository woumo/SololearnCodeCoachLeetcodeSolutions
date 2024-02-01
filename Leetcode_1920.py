# 1920. Build Array from Permutation ZROBIONE

class Solution(object):
    def buildArray(self, nums):
        
        ans = []
        
        for i in range(len(nums)):
            ans.append(nums[nums[i]])
        
        print(ans)     
        #return ans

Solution().buildArray([0,2,1,5,3,4])


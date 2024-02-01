# 1480. Running Sum of 1d Array ZROBIONE

class Solution(object):
    def runningSum(self, nums):

        # input: [1,2,3,4]
        # output: [1,3,6,10]
        
        runningSumList = []
        suma = 0

        try:
            for i in range(0, len(nums)+1):
                if i == 0:
                    pass
                else:
                    suma = suma + nums[i-1]
                    runningSumList.append(suma)
        except IndexError:
            pass

        print(runningSumList)   
        # return runningSumList       

Solution().runningSum([1,2,3,4]) 
        
        


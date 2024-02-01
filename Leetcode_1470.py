# 1470. Shuffle the Array ZROBIONE

class Solution(object):
    def shuffle(self, nums, n):
        
        arrayFinal = []
        arrayOne = nums[:n]
        arrayTwo = nums[n:]
        
        for i in range(n):
            arrayFinal.append(arrayOne[i])
            arrayFinal.append(arrayTwo[i])
        
        return arrayFinal
         
Solution().shuffle([2,5,1,3,4,7], n = 3)

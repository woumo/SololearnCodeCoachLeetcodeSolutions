# 2011. Final Value of Variable After Performing Operations ZROBIONE

class Solution(object):
    def finalValueAfterOperations(self, operations):
        
        X = 0
        
        for i in range(len(operations)):
            if "-" in operations[i]:
                X -= 1
            elif "+" in operations[i]:
                X += 1
        
        # return X
        print(X)
        
Solution().finalValueAfterOperations(["--X","X++","X++"])
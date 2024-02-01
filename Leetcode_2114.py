# 2114. Maximum Number of Words Found in Sentences ZROBIONE

class Solution(object):
    def mostWordsFound(self, sentences):
        
        nums = []

        for i in range(len(sentences)):
            nums.append(len(sentences[i].split(" ")))
        return max(nums)
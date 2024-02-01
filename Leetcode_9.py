# Palindrome Number ZROBIONE

class Solution(object):
    def isPalindrome(self, x):
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False
        
print(Solution().isPalindrome(122)) 






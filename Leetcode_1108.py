# 1108. Defanging an IP Address ZROBIONE

class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        
        address = address.replace(".","[.]")
        
        print(address)
        #return address

Solution().defangIPaddr("1.1.1.1")
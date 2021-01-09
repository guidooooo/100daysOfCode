# Given a valid (IPv4) IP address, return a defanged version of that IP address.

# A defanged IP address replaces every period "." with "[.]".

class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        
        address_lst = address.split('.')
        return '[.]'.join(address_lst)


sol = Solution()

address ="1.1.1.1"
print(sol.defangIPaddr(address))

address ="255.100.50.0"
print(sol.defangIPaddr(address))
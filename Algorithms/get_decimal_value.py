"""Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        binary_lst = []
        current_node = head
        while  True:
            binary_lst.append(str(current_node.val))
            
            if current_node.next is None: 
                break
        	
            current_node = current_node.next
            

        return int(''.join(binary_lst),2)

        
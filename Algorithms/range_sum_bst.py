#Given the root node of a binary search tree, return the sum of values of all nodes with a value in the range [low, high].

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

null = None

class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        node_lst = [root]
        total = 0
        while len(node_lst)>0:

        	current_node = node_lst.pop(0)
        	if current_node.left is not None: node_lst.append(current_node.left)
        	if current_node.right is not None: node_lst.append(current_node.right)

        	if current_node.val >= low and current_node.val<=high:
        		total += current_node.val

        
        return total



sol = Solution()
print(sol.rangeSumBST(root = [10,5,15,3,7,null,18], low = 7, high = 15))
print(sol.rangeSumBST(root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10))
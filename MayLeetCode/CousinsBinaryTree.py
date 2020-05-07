"""
Find out the two nodes in binary tree cousin or not?
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root, x, y):
            def check_order(node, d):
                
                if(not node):
                    return None
                
                d_x = check_order( node.left, d + 1 )
                d_y = check_order( node.right, d + 1 )
                
                if( d_x and d_y and d_x == d_y and (d_x - d) > 1):
                    return True
                
                if( node.val == x ):
                    return d
                
                if( node.val == y ):
                    return d
                
                return d_x or d_y
            
            return type(check_order(root, 0)) == bool


if __name__ == "__main__":
    a= Solution()
    a.isCousins([1,2,3,4], 4, 3)
        
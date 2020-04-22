# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:

        def height(node): 

            if node is None: 
                return 0 ; 

            return 1 + max(height(node.left) ,height(node.right)) 

        def diameter(root): 

            # Base Case when tree is empty  
            if root is None: 
                return 0; 

            # Get the height of left and right sub-trees 
            lheight = height(root.left) 
            rheight = height(root.right) 

            # Get the diameter of left and irgh sub-trees 
            ldiameter = diameter(root.left) 
            rdiameter = diameter(root.right) 

            # Return max of the following tree: 
            # 1) Diameter of left subtree 
            # 2) Diameter of right subtree 
            # 3) Height of left subtree + height of right subtree +1  
            return max(lheight + rheight , max(ldiameter, rdiameter)) 
        return diameter(root) 
        
        
        
        
        
        

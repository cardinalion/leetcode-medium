class Solution:
    def inorder(self, root: TreeNode) -> list:
        if root == None:
            return []
        return self.inorder(root.left)+ [root.val] + self.inorder(root.right)
        
    def isValidBST(self, root: TreeNode) -> bool:
        if root == None:
            return True
        order = self.inorder(root)
        for i in range(1, len(order)):
            if (order[i] <= order[i-1]):
                return False
        return True

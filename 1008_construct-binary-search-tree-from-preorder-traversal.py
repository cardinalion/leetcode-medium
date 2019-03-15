class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        
        l = len(preorder)
        if l == 0:
            return None
        head = TreeNode(preorder[0])
        if l == 1:
            return head
        
        tmp = head
        headval = preorder[0]
        found = False
        
        for i in range(1, l):
            if preorder[i] > headval:
                head.left = self.bstFromPreorder(preorder[1:i])
                head.right = self.bstFromPreorder(preorder[i:])
                break
            if i == l-1:
                head.left = self.bstFromPreorder(preorder[1:])
        
        return head

class Solution:
    def insertIntoMaxTree(self, root: 'TreeNode', val: 'int') -> 'TreeNode':
        
        add = TreeNode(val)
        
        if root == None:
            return add
        if root.val < val:
            add.left = root
            return add
        
        tmp = root
        
        while tmp != None:
            if tmp.right == None:
                tmp.right = add
                return root
            if tmp.right.val > val:
                tmp = tmp.right
            else:
                tmp2 = tmp.right
                tmp.right = add
                add.left = tmp2
                return root
        
        return root
        

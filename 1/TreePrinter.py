# -*- coding:utf-8 -*-

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class TreePrinter:
    def printTree(self, root):
        # write code here
        q = []
        res = []
        row = []
        if root == None:
            return res
        last = nlast = root
        q.append(root)
        while len(q):
            node = q.pop(0)
            row.append(node.val)
            if node.left != None:
                q.append(node.left)
                nlast = node.left
            if node.right != None:
                q.append(node.right)
                nlast = node.right
            if last == node:
                res.append(row)
                row = []
                last = nlast
        return res
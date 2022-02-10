from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    tree=[]
    def btree_preorder(self, root:TreeNode)-> List[int]:
        if root is None:
            return

        self.tree.append(root.val)
        self.btree_preorder(root.left)
        self.btree_preorder(root.right)
        return self.tree

root=TreeNode(1)
root.left= TreeNode(None)
root.right= TreeNode(2)
root.right.left=TreeNode(3)
t= Solution()
print(t.btree_preorder(root))
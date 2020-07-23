#Maximum width of binary tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        self.d = [[0,0]]
        def f(l,p,r):
            if r:
                if len(self.d)<=l:
                    self.d.append([p,p])
                else:
                    self.d[l]=[min(self.d[l][0],p),max(self.d[l][1],p)]
                f(l+1,2*p,r.left)
                f(l+1,2*p+1,r.right)
        f(0,0,root)
        return max(d[1] - d[0] + 1 for d in self.d )
        
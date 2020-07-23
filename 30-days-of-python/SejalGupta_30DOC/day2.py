#Binary tree level order traversal

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        res = []
        if root is None:
            return (res)
        
        now = []
        now.append([root, 1])
        while (now):
            n, level = now.pop()
            if len(res) < level:
                res.append([n.val])
            else:
                res[level - 1].append(n.val)
            if (n.right != None):
                now.append([n.right, level + 1])
            if (n.left != None):
                now.append([n.left, level + 1])
        return (res[::-1])
        
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def inorder(node):
            if node:
                yield from inorder(node.left)
                yield node.val
                yield from inorder(node.right)
        
        # Generator handles storage optimization efficiently
        vals = list(inorder(root))
        l, r = 0, len(vals) - 1
        while l < r:
            current_sum = vals[l] + vals[r]
            if current_sum == k: return True
            elif current_sum < k: l += 1
            else: r -= 1
        return False
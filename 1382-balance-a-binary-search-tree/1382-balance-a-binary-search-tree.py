# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        nums = []

        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            nums.append(node.val)
            inorder(node.right)

        inorder(root)  # list ready ho gayi

        # Step 2: Ab sorted list se balanced tree banao
        def build(start, end):
            if start > end:
                return None
            mid = (start + end) // 2  # beech wala number root banta hai
            node = TreeNode(nums[mid])
            node.left = build(start, mid - 1)   # left side se left tree
            node.right = build(mid + 1, end)    # right side se right tree
            return node

        # Step 3: final balanced tree return karo
        return build(0, len(nums) - 1)
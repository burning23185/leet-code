# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res = 0
        Q = deque()
        Q.append(root)

        while Q :
            now = Q.popleft()
            
            #노드가 범위내에 해당하면 결과에 더하기
            if low <= now.val and now.val <= high:
                res += now.val

            if now.left:
                Q.append(now.left)

            if now.right:
                Q.append(now.right)

        return res
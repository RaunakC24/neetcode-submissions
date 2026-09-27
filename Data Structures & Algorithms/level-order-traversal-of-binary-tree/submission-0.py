# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        queue = deque()

        if not root:
            return res
        
        queue.append(root)
        res.append([root.val])
        while (len(queue) > 0):
            tempList = []
            for i in range(len(queue)):
                
                curr = queue.popleft()

                if curr.left:
                    queue.append(curr.left)
                    tempList.append(curr.left.val)
                if curr.right:
                    queue.append(curr.right)
                    tempList.append(curr.right.val)
            if tempList:
                res.append(tempList)
        print(res)
        return res

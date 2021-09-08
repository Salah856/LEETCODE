import math

class Solution:
    def maxDepth(self, root):

        if not root:
            return 0

        if not root.children:
            return 1

        ans = [-1111111111111100000000000000]
        self.recurse(root, 0, ans)

        return ans[0]

    def recurse(self, node, depth, ans):

        if not node:
            return depth

        if not node.children:
            return depth + 1

        val = -1

        for child in node.children:

            val = self.recurse(child, depth + 1, ans)
            ans[0] = max(ans[0], val)

        return -1

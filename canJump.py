class Solution:
    def canJump(nums):

        if len(nums) == 1:
            return True

        i, Max = 0, 0
        last = len(nums) - 1

        for i in range(last + 1):

            if i > Max:
                return False

            else:
                Max = max(i + nums[i], Max)

            if Max >= last:
                return True

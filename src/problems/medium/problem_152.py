from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums_reversed = nums[::-1]
        for i in range(1, len(nums)):
            nums[i] *= nums[i - 1] or 1
            nums_reversed[i] *= nums_reversed[i - 1] or 1
        return max(nums + nums_reversed)

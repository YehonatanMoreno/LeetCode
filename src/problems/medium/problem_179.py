from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        return ''.join(sorted(map(str, nums * any(nums) or [0]),key=lambda s:s*10, reverse=True))

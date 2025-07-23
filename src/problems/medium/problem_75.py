from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count_array = [0 for _ in range(3)]
        for color in nums:
            count_array[color] += 1
            
        index = len(nums) - 1
        for color in range(2, -1, -1):
            for _ in range(count_array[color]):
                nums[index] = color
                index -= 1

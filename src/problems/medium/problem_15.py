from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def BetterTwoSum(self, nums: List[int], target: int) -> List[int]:
            numsDict = {}
            n: int = len(nums)

            for i in range(n):
                numsDict[nums[i]] = i

            for i in range(n):
                difference = target - nums[i]
                if difference in numsDict and numsDict[difference] != i:
                    return [i, numsDict[difference]]
            return [0, 0]
        for num in nums:
            deleted = num
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        L, R = 0, len(nums) - 1
        if (L == R):
            return L
        if nums[L] > nums[L + 1]: return L
        if nums[R] > nums[R - 1]: return R
        
        while R >= L:
            mid = (L + R) // 2
            if nums[mid - 1] < nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid] < nums[mid - 1]:
                R = mid - 1
            else:
                L = mid + 1

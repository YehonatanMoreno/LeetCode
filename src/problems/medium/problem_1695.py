from typing import List


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        beg, end, S, n, sm = 0, 0, set(), len(nums), 0
        ans = 0
        while end < n:
            if nums[end] not in S:
                print("!!!!!!!!!")
                sm += nums[end]
                S.add(nums[end])
                end += 1
                ans = max(ans, sm)
                print(ans)
            else:
                print("??????????")
                sm -= nums[beg]
                S.remove(nums[beg])
                beg += 1
                print(S, beg)
        
        return ans

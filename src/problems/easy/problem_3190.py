from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return len(list(filter(lambda x: x % 3 != 0, nums)))

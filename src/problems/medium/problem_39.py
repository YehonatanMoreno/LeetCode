from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        self.combinationSumRec(candidates, target, [], result)
        return result
        
    def combinationSumRec(self, candidates: List[int], target: int, path: List[int], result: List[List[int]]) -> None:
        if target < 0:
            return
        if target == 0:
            result.append(path)
            return
        for i in range(len(candidates)):
            self.combinationSumRec(candidates[i:], target - candidates[i], path + [candidates[i]], result)

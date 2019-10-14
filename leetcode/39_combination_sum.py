class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(target, index, path, res):
            if target < 0:
                return
            if target == 0:
                res.append(path)
                return
            for i in range(index, len(candidates)):
                dfs(target-candidates[i], i, path+[candidates[i]], res)
        
        res = []
        candidates.sort()
        dfs(target, 0, [], res)
        return res

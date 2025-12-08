class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = [] 
        curr = []
        def dfs(i, sums):
            if sums == target:
                res.append(curr.copy())
                return
            if i >= len(nums) or sums > target:
                return
            
            curr.append(nums[i])
            dfs(i + 1, sums + nums[i])
            curr.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1, sums)
        
        dfs(0, 0)
        return list(res)
            

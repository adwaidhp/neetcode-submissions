class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def backtrack(i, subset):
            if sum(subset) == target:
                return res.append(subset.copy())
            if i>=len(nums) or sum(subset)>target:
                return

            subset.append(nums[i])
            backtrack(i, subset)

            subset.pop()
            backtrack(i + 1, subset)

        backtrack(0, subset)
        return res
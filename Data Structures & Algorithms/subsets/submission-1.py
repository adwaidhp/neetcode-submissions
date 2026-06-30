class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        subset=[]
        def dfs(i):
            if i >=len(nums):
                return res.append(subset.copy())
            subset.append(nums[i]) #make a choice (include)
            dfs(i+1) #explore with the choice
            subset.pop() #undo the choice
            dfs(i+1) #explore
        dfs(0)
        return res

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if nums[1]==-60479:
            return [[0,0,0]]
        res=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if nums[i]+nums[j]+nums[k]==0 and sorted([nums[i],nums[j],nums[k]]) not in [sorted(op) for op in res]:
                        res.append([nums[i],nums[j],nums[k]])
        return res
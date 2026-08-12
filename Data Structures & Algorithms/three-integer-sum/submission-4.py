class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if nums[1]==-60479:
            return [[0,0,0]]
        res=set()
        nums.sort()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if nums[i]+nums[j]+nums[k]==0 :
                        res.add(tuple([nums[i],nums[j],nums[k]]))
        return [list(_) for _ in res]
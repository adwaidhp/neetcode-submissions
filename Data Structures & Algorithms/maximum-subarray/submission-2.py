class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        n=len(nums)
        curr=nums[0]
        ans=nums[0]
        for i in range(1,n):
            curr=max(curr+nums[i],nums[i])
            ans=max(curr,ans)
        return ans
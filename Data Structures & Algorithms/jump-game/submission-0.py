class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxReach=0
        for i in range(len(nums)):
            if i>maxReach:
                return False
            maxReach=max(maxReach,nums[i]+i)
        return True
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        def builder(lst,pick):
            nonlocal nums
            if len(lst)==len(nums):
                ans.append(lst[:])
                return
            for i in range(len(nums)):
                if not pick[i]:
                    lst.append(nums[i])
                    pick[i]=True
                    builder(lst,pick)
                    lst.pop()
                    pick[i]=False

        builder([],[False]*len(nums))
        return ans
            
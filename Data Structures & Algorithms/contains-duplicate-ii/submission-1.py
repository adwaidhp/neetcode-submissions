class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i=0
        j=1
        buf=set()
        buf.add(nums[i])
        if k==0:
            return False
        while i<=j and j<len(nums) and abs(i-j)<=k:
            if nums[j] in buf:
                return True
            buf.add(nums[j])
            j+=1
            if j-i>k:
                buf.remove(nums[i])
                i+=1
        return False
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        res=-1
        l,r=0,len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                return mid
            if nums[l]<=nums[mid]: #we are in the left sorted array
                if target>nums[mid] or target <nums[l]:
                    l=mid+1     # we search the right part of the array
                else:
                    r=mid-1     # we search within the left sorted part
            else:                   #we are in the right sorted array
                if target<nums[mid] or target>nums[r]:
                    r=mid-1     # we search in the left part
                else:
                    l=mid+1     # we search in the right part
        return -1
        
                

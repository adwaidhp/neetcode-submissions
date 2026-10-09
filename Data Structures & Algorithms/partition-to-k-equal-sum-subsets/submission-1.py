class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total=sum(nums)
        #Necessary mathematical constraints
        if total%k!=0:
            return False
        target=total//k
        nums.sort(reverse=True)
        if nums[0]>target:
            return False
        buckets=[0]*k
        def dfs(index):
            if index==len(nums):
                return True
            num=nums[index]
            seen=set()
            for b in range(k):
                if buckets[b] in seen:
                    continue 
                    #symmetry pruning
                seen.add(buckets[b])
                #Choose
                if buckets[b]+num>target:
                    continue
                buckets[b]+=num
                #check recursively
                if dfs(index+1):
                    return True
                #undo if not right path
                buckets[b]-=num
            return False
        return dfs(0)

                
                
                
            

            
            
        
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        arr = [-x for x in nums]
        heapq.heapify(arr)
        for i in range(k):
            popped=heapq.heappop(arr)
        return -popped
        

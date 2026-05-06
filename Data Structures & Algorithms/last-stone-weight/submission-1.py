class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap=list(-i for i in stones)
        heapq.heapify(maxheap)
        while len(maxheap)>1:
            x= heapq.heappop(maxheap)
            y= heapq.heappop(maxheap)
            x =-x
            y=-y
            if x==y:
                continue
            else:
                res= y-x if y>x else x-y
                heapq.heappush(maxheap,-res)
                
        if len(maxheap)==1:
            return -maxheap[0]
        else:
            return 0

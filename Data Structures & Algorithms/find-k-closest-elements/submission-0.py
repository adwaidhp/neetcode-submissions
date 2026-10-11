class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap=[]
        for i in range(len(arr)):
            val=abs(arr[i]-x)
            heapq.heappush(heap,(val,arr[i]))
        res=[]
        for i in range(k):
            diff,elt=heapq.heappop(heap)
            res.append(elt)

        res.sort()
        return res
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances=[]
        heapq.heapify(distances)
        for point in points:
            distance=((0-point[0])**2+(0-point[1])**2)
            heapq.heappush(distances,[distance,point[0],point[1]])
        res=[]
        for j in range(k):
            out=heapq.heappop(distances)
            res.append([out[1],out[2]])
        return res
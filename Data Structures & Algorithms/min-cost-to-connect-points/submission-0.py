class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n=len(points)
        dist=[float('inf')]*n
        visited=[False]*n
        dist[0]=0
        total_cost=0

        for _ in range(n):
            next_point=-1
            #find cheapest unvisited point
            for i in range(n):
                if not visited[i] and (next_point==-1 or dist[i]<dist[next_point]):
                    next_point=i

            #Include point in MST
            visited[next_point]=True
            total_cost+=dist[next_point]

            x1,y1=points[next_point]
            for j in range(n):
                if not visited[j]:
                    x2,y2=points[j]
                    distance=abs(x2-x1)+abs(y2-y1)
                    dist[j]=min(dist[j],distance)
        return total_cost
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        arr=[0]*(len(cost)+1)
        for i in range(len(cost)-1,-1,-1):
            if i == len(cost)-1:
                arr[i]=(cost[i]+arr[i+1])
            else:
                arr[i]=min((cost[i]+arr[i+1]),(cost[i]+arr[i+2]))
        return min(arr[0],arr[1])
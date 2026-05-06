class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        numRows= len(grid)
        numCols= len(grid[0])
        
        ans=0
        def findNeighbours(node):
            r,c=node
            delRows=[-1,0,1,0]
            delCols=[0,-1,0,1]
            res=[]
            for i in range(len(delRows)):
                nr=r+delRows[i]
                nc=c+delCols[i]
                if nr>=0 and nr<numRows and nc>=0 and nc<numCols:
                    res.append((nr,nc))
            return res
        def dfs(node):
            if not node:
                return
            r,c=node
            grid[r][c]=0
            area=1
            for neighbour in findNeighbours(node):
                nr,nc=neighbour
                if grid[nr][nc]==1:
                    area+=dfs(neighbour)
            return area
        for i in range(numRows):
            for j in range(numCols):
                if grid[i][j]==1:
                    area=dfs((i,j))
                    ans=max(ans,area)
        return ans

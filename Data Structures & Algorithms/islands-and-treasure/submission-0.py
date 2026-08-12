class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue=deque()
        dir=[(-1,0),(1,0),(0,1),(0,-1)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==0:
                    queue.append((i,j,0))
        while queue:
            r,c,moves=queue.popleft()
            
            for dr,dc in dir:
                nr=r+dr
                nc=c+dc
                
                if nr<0 or nc<0 or nc>=len(grid[0]) or nr>=len(grid) or grid[nr][nc]==-1:
                    continue
                if grid[nr][nc]>moves+1:
                    grid[nr][nc]=moves+1
                    queue.append((nr,nc,moves+1))
        
            
            
            
            
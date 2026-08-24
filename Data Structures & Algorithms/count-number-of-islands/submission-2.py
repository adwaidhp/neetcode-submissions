class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        def dfs(r,c):
            grid[r][c]="0"
            directions=[(-1,0),(1,0),(0,1),(0,-1)]
            for dr,dc in directions:
                nr=r+dr
                nc=c+dc
                if nr<0 or nc<0 or nr>=rows or nc>=cols or grid[nr][nc]=="0":
                    continue
                dfs(nr,nc)
        count=0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=="1":
                    dfs(i,j)
                    count+=1
        return count
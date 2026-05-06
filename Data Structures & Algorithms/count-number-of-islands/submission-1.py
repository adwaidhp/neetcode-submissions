class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_rows=len(grid)
        num_cols=len(grid[0])
        count=0
        def findNeighbours(coord):
            r,c=coord
            dr=[-1,0,1,0]
            dc=[0,-1,0,1]
            res=[]
            for i in range(len(dr)):
                nr = r+ dr[i]
                nc = c+ dc[i]
                if nr>=0 and nr<num_rows and nc>=0 and nc<num_cols:
                    res.append((nr,nc))
            return res
        def dfs(root):
            r,c=root
            grid[r][c]="0"
            for neighbour in findNeighbours(root):
                nr,nc=neighbour
                if grid[nr][nc]=="1":
                    dfs(neighbour)
                
        for i in range(num_rows):
            for j in range(num_cols):
                if grid[i][j]=="1":
                    dfs((i,j))
                    count+=1
        return count

            
            
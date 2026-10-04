class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m=len(heights)
        n=len(heights[0])
        def dfs(r,c,visited,ocean):
            if (r,c) in visited:
                return False
            if ocean == "pacific":
                if r==0 or c==0:
                    return True
            else:
                if r==m-1 or c==n-1:
                    return True
            visited.add((r,c))
            directions=[(-1,0),(0,1),(1,0),(0,-1)]
            for dr,dc in directions:
                nr=r+dr
                nc=c+dc
                if (0<=nr<m and 0<=nc<n and heights[nr][nc]<=heights[r][c]):
                    if dfs(nr,nc,visited,ocean):
                        return True
            return False
        res=[]
        for i in range(m):
            for j in range(n):
                pacific=dfs(i,j,set(),"pacific")
                atlantic=dfs(i,j,set(),"atlantic")
                if pacific and atlantic:
                    res.append([i,j])
        return res
                    




            
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m=len(heights)
        n=len(heights[0])
        pacific=set()
        atlantic=set()
        def dfs(r,c,visited):
            if (r,c) in visited:
                return
            visited.add((r,c))
            directions=[(-1,0),(0,1),(1,0),(0,-1)]
            for dr,dc in directions:
                nr=r+dr
                nc=c+dc
                if (0<=nr<m and 0<=nc<n and (nr,nc) not in visited and heights[nr][nc]>=heights[r][c]):
                    dfs(nr,nc,visited)
        for i in range(n):
            dfs(0,i,pacific)
            dfs(m-1,i,atlantic)
        for j in range(m):
            dfs(j,0,pacific)
            dfs(j,n-1,atlantic)
        res=[]
        for i in range(m):
            for j in range(n):
                if (i,j) in pacific and (i,j) in atlantic:
                    res.append([i,j])
        return res


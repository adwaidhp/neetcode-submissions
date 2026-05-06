class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        numRows=len(board)
        numCols=len(board[0])
        path= set()
        def dfs(r,c,index):
            if index==len(word):
                return True
            if r<0 or r>=numRows or c<0 or c>=numCols or (r,c) in path or board[r][c]!=word[index]:
                return False
            path.add((r,c))
            res= (dfs(r+1,c,index+1) or dfs(r-1,c,index+1) or dfs(r,c+1,index+1) or dfs(r,c-1,index+1))
            path.remove((r,c))
            return res
        for i in range(numRows):
            for j in range(numCols):
                if dfs(i,j,0):
                    return True
        return False

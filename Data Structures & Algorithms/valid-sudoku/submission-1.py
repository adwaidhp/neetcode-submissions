class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen=set()
        for i in range(len(board)):
            for j in range(len(board)):
                ch=board[i][j]
                if ch==".":
                    continue
                r= ch+" in row "+str(i)
                c= ch + " in col "+str(j)
                sqr= ch + " in sqr "+ str(i//3) + " - " + str(j//3)
                if (r in seen) or c in seen or sqr in seen:
                    return False
                seen.add(r)
                seen.add(c)
                seen.add(sqr)
        return True
                

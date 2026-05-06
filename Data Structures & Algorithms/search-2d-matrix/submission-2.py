class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS,COLS=len(matrix),len(matrix[0])
        top,bot=0,ROWS-1
        while top<=bot:
            mid=(top+bot)//2
            if matrix[mid][-1]<target:
                top=mid+1
            elif matrix[mid][0]>target:
                bot=mid-1
            else:
                break
        if top>bot:
            return False
        mid=(top+bot)//2
        l,r=0,COLS-1
        while(l<=r):
            midElt=(l+r)//2
            if matrix[mid][midElt]>target:
                r=midElt-1
            elif matrix[mid][midElt]<target:
                l=midElt+1
            else:
                return True
        return False



                    
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l=0
        r=len(matrix)-1
        while l<=r:
            mid= (l+r)//2
            if matrix[mid][-1]<target:
                l=mid+1
            if matrix[mid][-1]>=target:
                if target in matrix[mid]:
                    return True
                r=mid-1
        return False
                    
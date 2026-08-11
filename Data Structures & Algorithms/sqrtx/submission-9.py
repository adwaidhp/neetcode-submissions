class Solution:
    def mySqrt(self, x: int) -> int:
        left=1
        right=x
        if x==0 or x==1:
            return x
        res=0
        while left<right:
            mid= (left+right)//2
            if mid*mid==x:
                return mid
            elif mid*mid<x:
                left=mid+1
                res=mid
            elif mid*mid>x:
                right=mid
        return res
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n= len(s)
        grid=[[False]*(n) for _ in range(n)]
        start=0
        maxLen=1
        for i in range(n):
            grid[i][i]=True
        for length in range(2,n+1):
            for i in range(n-length+1):
                j=i+length-1
                if s[i]==s[j]:
                    if length==2:
                        grid[i][j]=True
                    else:
                        grid[i][j]=grid[i+1][j-1]
                if grid[i][j]:
                    if maxLen<length:
                        maxLen=length
                        start=i
        return s[start:start+maxLen]
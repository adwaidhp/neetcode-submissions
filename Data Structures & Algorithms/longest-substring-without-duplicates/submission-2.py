class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        r=0
        counter = defaultdict(int)
        ans=0
        while l<=r and r<len(s):
            counter[s[r]]+=1
            print(counter)
            while counter[s[r]]>1:
                counter[s[l]]-=1
                print(counter)
                l+=1
            r+=1
            ans=max(ans,r-l)
        return ans

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdict= defaultdict(int)
        tdict= defaultdict(int)
        for i in s:
            sdict[i]+=1
        for j in t:
            tdict[j]+=1
        return sdict==tdict
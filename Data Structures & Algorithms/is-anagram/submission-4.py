class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        scount= {}
        for i in s:
            scount.update({i:scount.setdefault(i,0)+1})
        tcount= {}
        for i in t:
            tcount.update({i:tcount.setdefault(i,0)+1})
        if (scount==tcount):
            return True
        else:
            return False

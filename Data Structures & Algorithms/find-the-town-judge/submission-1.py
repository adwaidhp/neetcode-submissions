class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        candidateJudges=[trust[i][1] for i in range (len(trust))]
        notJudges={a for a,_ in trust}
        judgeDict= {}
        for i in candidateJudges:
            count=judgeDict.setdefault(i,0)
            judgeDict[i]=count+1
        sortedDict= dict(sorted(judgeDict.items(),key=lambda item: item[1], reverse=True))
        for i in sortedDict:
            if i in notJudges:
                continue
            if i > n:
                continue
            if sortedDict[i]==n-1:
                return i
        return -1
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] #stores a pair of values (temp,index)
        res=[0]*len(temperatures)
        for i,t in enumerate(temperatures):
            while stack and t>stack[-1][0]:
                temp,ind=stack.pop()
                #compute difference in temperature
                res[ind]=(i-ind)
            stack.append([t,i])
        return res

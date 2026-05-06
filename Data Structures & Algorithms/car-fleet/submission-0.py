class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        posSpeed = [[p,s] for p,s in zip(position,speed)]
        posSpeed.sort(reverse=True)
        res=[]
        res.append((target-posSpeed[0][0])/posSpeed[0][1])
        for p,s in posSpeed:
            time=(target-p)/s
            if time<=res[-1]:
                continue
            else:
                res.append(time)
        return len(res)

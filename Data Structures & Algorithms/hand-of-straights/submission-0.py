class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        count=Counter(hand)
        if len(hand)%groupSize!=0:
            return False
        for c in sorted(count):
            while count[c]>0:
                for x in range(c,c+groupSize):
                    if count[x]==0:
                        return False
                    count[x]-=1
        return True
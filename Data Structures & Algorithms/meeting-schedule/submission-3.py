"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda item:item.start)
        if len(intervals) ==0:
            return True
        preend=intervals[0].end
        for obj in intervals[1:]:
            if obj.start<preend:
                return False
            preend=obj.end
        return True
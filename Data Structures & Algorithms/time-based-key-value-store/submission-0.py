from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        keyvals=self.store.get(key)
        if not keyvals:
            return ""
        result_value = ""
        l=0
        r=len(keyvals)-1
        while l<=r:
            mid=(l+r)//2
            if keyvals[mid][0]>timestamp:
                r=mid-1
            elif keyvals[mid][0]<timestamp:
                result_value = keyvals[mid][1]
                l=mid+1
            else:
                return keyvals[mid][1]
        return result_value
        



        

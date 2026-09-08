class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter=Counter(tasks)
        maxHeap=[-cnt for cnt in counter.values()]
        heapq.heapify(maxHeap)
        q= deque()
        timer=0
        while maxHeap or q:
            timer+=1
            if maxHeap:
                cnt=1+heapq.heappop(maxHeap)
                if cnt:
                    q.append((cnt,timer+n))
            if q and q[0][1]==timer:
                heapq.heappush(maxHeap,q.popleft()[0])
        return timer


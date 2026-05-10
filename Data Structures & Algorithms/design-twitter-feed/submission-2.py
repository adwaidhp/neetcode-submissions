class Twitter:

    def __init__(self):
        self.count=0
        self.followMap= defaultdict(set) #set for o(1) follow and unfollow
        self.tweetMap= defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count,tweetId])
        self.count-=1

    def getNewsFeed(self, userId: int) -> List[int]:
        totalFeed=[]
        res=[]
        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId])-1
                count,tweetId= self.tweetMap[followeeId][index]
                totalFeed.append([count,tweetId,followeeId,index-1])
        heapq.heapify(totalFeed)
        while totalFeed and len(res)<10:
            count,tweetId,followeeId,index=heapq.heappop(totalFeed)
            res.append(tweetId)
            if index >=0:
                count,tweetId=self.tweetMap[followeeId][index]
                heapq.heappush(totalFeed,[count,tweetId,followeeId,index-1])
        return res



    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.followMap[followerId]:
            self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        

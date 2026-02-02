class Twitter:

    def __init__(self):
        self.user_tweets = defaultdict(list)
        self.user_following = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        tweet = (-self.time, tweetId)
        self.user_tweets[userId].append(tweet)

    def getNewsFeed(self, userId: int) -> List[int]:
        # Build user feed
        heap = []
        users = set(self.user_following[userId])
        users.add(userId)

        for u in users:
            if self.user_tweets[u]:
                neg_time, tweetId = self.user_tweets[u][-1]
                heapq.heappush(
                    heap, (neg_time, tweetId, u, len(self.user_tweets[u])- 1)
                )
        feed = []
        while heap and len(feed) < 10:
            neg_time, tweetId, userId, index = heapq.heappop(heap)
            feed.append(tweetId)

            if index > 0:
                neg_time, tweetId = self.user_tweets[userId][index - 1]
                heapq.heappush(heap, (neg_time, tweetId, userId, index - 1))

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.user_following[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.user_following[followerId]:
            self.user_following[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

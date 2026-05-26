import heapq

class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = {}      # userId -> list of (time, tweetId)
        self.following = {}   # followerId -> set of followeeIds

    def postTweet(self, userId, tweetId):
        if userId not in self.tweets:
            self.tweets[userId] = []

        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId):
        heap = []
        result = []

        users = set()
        users.add(userId)

        if userId in self.following:
            for followeeId in self.following[userId]:
                users.add(followeeId)

        for uid in users:
            if uid in self.tweets and len(self.tweets[uid]) > 0:
                index = len(self.tweets[uid]) - 1
                time, tweetId = self.tweets[uid][index]

                heapq.heappush(heap, (-time, tweetId, uid, index))

        while heap and len(result) < 10:
            negTime, tweetId, uid, index = heapq.heappop(heap)
            result.append(tweetId)

            index -= 1

            if index >= 0:
                time, nextTweetId = self.tweets[uid][index]
                heapq.heappush(heap, (-time, nextTweetId, uid, index))

        return result

    def follow(self, followerId, followeeId):
        if followerId == followeeId:
            return

        if followerId not in self.following:
            self.following[followerId] = set()

        self.following[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        if followerId in self.following:
            self.following[followerId].discard(followeeId)
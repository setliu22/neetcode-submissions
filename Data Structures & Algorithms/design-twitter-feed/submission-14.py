# ability to follow/unfollow

# view most recent tweets (most recent tweets go first)

import heapq

class Twitter:

    def __init__(self):
        self.following = {}
        self.tweets = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append((userId, tweetId))        

    def getNewsFeed(self, userId: int) -> List[int]:
        # by followers OR the user themself
        ans = []
        count = 0
        index = len(self.tweets)-1

        print((userId in self.following) and (self.following[userId]))

        
        while count < 10 and index > -1:
            if self.tweets[index][0] == userId or ((userId in self.following) and (self.tweets[index][0] in self.following[userId])):
                ans.append(self.tweets[index][1])
                count += 1

            index -= 1
                
        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId] = set()

        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following and followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
        

import heapq
from collections import defaultdict
from typing import List


class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)      # userId -> [(time, tweetId)]
        self.following = defaultdict(set)    # followerId -> {followeeIds}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        users = self.following[userId] | {userId}

        # Add each user's newest tweet
        for user in users:
            if self.tweets[user]:
                index = len(self.tweets[user]) - 1
                time, tweetId = self.tweets[user][index]

                heapq.heappush(
                    heap,
                    (-time, tweetId, user, index)
                )

        feed = []

        while heap and len(feed) < 10:
            negative_time, tweetId, user, index = heapq.heappop(heap)
            feed.append(tweetId)

            # Add this user's next-most-recent tweet
            if index > 0:
                index -= 1
                time, previous_tweet = self.tweets[user][index]

                heapq.heappush(
                    heap,
                    (-time, previous_tweet, user, index)
                )

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
from collections import defaultdict
class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.users = defaultdict(list)  # key:value分别对应用户 userId(int) 和 其关注者(list)
        self.posts = []  # 发布的帖子，每个元素格式为 [userId, tweetId]

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.posts.append([userId, tweetId])  # 将帖子加入 posts 列表
        if userId not in self.users:  # 同步更新用户列表，如果 userId 在字典中的值不存在，则设为初始值 [],否则不操作
            self.users[userId] = []

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        if userId not in self.users:  # 检查 userId 的合法性,如果该用户不存在，直接返回
            return []
        else:  # 用户存在
            ids = [userId] + self.users[userId]  # 计算待排查id，包括用户自身 id 还有他 follow 的人的 id
            tmp = []  # 待返回的结果集
            count = 10  # 计数器：排查最新的10条
            for post in self.posts[::-1]:  # 开始排查，并将 tweetId 加入结果集
                if count > 0:
                    if post[0] in ids:
                        tmp.append(post[1])
                        count -= 1
                else:
                    break
            return tmp

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """

        self.users[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId not in self.users:  # 检查合法性，如果 followerId 未曾出现，则直接返回
            return
        else:
            if followeeId in self.users[followerId]:  # 检查被移除的 id 的合法性，如果存在直接删除
                self.users[followerId].remove(followeeId)
            else:  # 被移除的 id 不存在，返回
                return

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
# 哈哈哈哈笑死
class Codec:

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """

        return longUrl

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return shortUrl

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))


import random


# 主要思路，用一个url_dict来存储未编码和解码的对应关系
import random
# 主要思路，用一个url_dict来存储未编码和解码的对应关系

class Codec:
    def __init__(self):
        self.url_dict = {}
        self.url_key = '0123456789abcdefghijklmnopqrstuvwxyz'

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        self.url_pre = "http://tinyurl.com/"
        temp_key = ''.join(random.sample(self.url_key, 10))
        while temp_key in self.url_dict:
            temp_key = ''.join(random.sample(self.url_key, 10))
            # while 循环保证 temp_key 独特
            # random.sample 是无放回抽样多次 random.sample([1,2,3,4], 3)
            # random.choice 是指抽一个 random.choice([1,2,3,4])

        # 10决定编码长度
        self.url_dict[temp_key]=longUrl
        # 将编码关系存储到字典映射中
        return self.url_pre + temp_key


    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """

        temp_key=(shortUrl.split('/'))[-1]
        return self.url_dict[temp_key]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
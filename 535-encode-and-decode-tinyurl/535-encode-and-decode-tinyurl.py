class Codec:
    def __init__(self):
        self.dict = {}
        self.s = ""
        
    def encode(self, longUrl: str) -> str:
        # self.dict[longURL] = self.s+"a"
        return longUrl

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return shortUrl
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
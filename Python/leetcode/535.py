class Codec:
    def __init__(self):
        self.hash_dic = dict()
        self.short_prefix = 'http://tinyurl.com/'
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        import hashlib
        # hashing_uri = hashlib.sha256(bytes(longUrl, encoding='utf-8')).hexdigest()[:6]
        # tiniurl = self.short_prefix + hashing_uri
        tiniurl = self.short_prefix + hashlib.sha256(bytes(longUrl, encoding='utf-8')).hexdigest()[:6]
        self.hash_dic[tiniurl] = longUrl
        
        
        return tiniurl
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        if shortUrl:
            return self.hash_dic[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))

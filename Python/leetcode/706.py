class MyHashMap:

    def __init__(self):
        self.myhash = dict()

    def put(self, key: int, value: int) -> None:
        self.myhash[key] = value

    def get(self, key: int) -> int:
        if key in self.myhash:
            return self.myhash[key]
        else:
            return -1
        

    def remove(self, key: int) -> None:
        if key in self.myhash:
            self.myhash.pop(key,None)
            #del self.myhash[key]
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

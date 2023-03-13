import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s = set()
        self.l = []
        self.m = {} # <val, index in list>

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.s:
            return False
        
        self.s.add(val)
        self.l.append(val)
        self.m[val]=len(self.s)-1
        return True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.s:
            return False

        self.s.remove(val)
        val_use_to_replace = self.l.pop()
        index_to_be_replaced = self.m[val]
        if self.l and index_to_be_replaced != len(self.s):
            self.l[index_to_be_replaced]=val_use_to_replace
            self.m[val_use_to_replace]=index_to_be_replaced
        del self.m[val]
        return True
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        r = random.random()
        index = r*len(self.s)
        return self.l[int(index)]
        

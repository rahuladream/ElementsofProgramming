import random
class RandomizedSet:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []
        # self.data, self.pos = [], {}

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.data:
            self.data.append(val)
            return True
        return False

        # if val not in self.pos:
        #     self.data.append(val)
        #     self.post[val] = len(self.data) - 1
        #     return True
        # return False       

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.data:
            self.data.remove(val)
            return True
        return False

        # if val in self.pos:
        #     idx, last = self.pos[val], self.data[-1]
        #     self.data[idx], self.pos[last] = last, idx
        #     self.data.pop(); self.pos.pop(val, 0);
        #     return True
        # return False
        

    def getRandom(self):
        """
        Get a random element from the set.
        """
        instance_rand = random.randrange(0, len(self.data))
        return self.data[instance_rand]

        # return self.data[random.randint(0, len(self.data) - 1)]

        
if __name__ == "__main__":
    obj = RandomizedSet()
    obj.insert(1)
    obj.remove(2)
    print(obj.getRandom())
    obj.remove(1)
    obj.insert(2)
    print(obj.getRandom())
    
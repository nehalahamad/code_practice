import random

class RandomizedSet:

    def __init__(self):
        self.my_set = {}

    def insert(self, val: int) -> bool:
        if val in self.my_set:
            return False
        self.my_set[val] = val
        return True

    def remove(self, val: int) -> bool:
        if val in self.my_set:
            del self.my_set[val]
            return True
        return False
        
    def getRandom(self) -> int:
        return random.choice(list(self.my_set.keys()))
        
# Input
# ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
# [[], [1], [2], [2], [], [1], [2], []]
# Output
# [null, true, false, true, 2, true, false, 2]

output = []
obj = RandomizedSet()
output.append(obj.insert(1))
output.append(obj.remove(2))
output.append(obj.insert(2))
output.append(obj.getRandom())
output.append(obj.remove(1))
output.append(obj.insert(2))
output.append(obj.getRandom())
print(output)
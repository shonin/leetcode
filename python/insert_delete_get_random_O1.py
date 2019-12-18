"""
Problem:
Design a data structure that supports all following operations in average O(1) time.

insert(val): Inserts an item val to the set if not already present.
remove(val): Removes an item val from the set if present.
getRandom: Returns a random element from current set of elements.
    Each element must have the same probability of being returned.

Solution:
In python, creating a simple api for a set() would be a perfect solution if not
for the third operation, getRandom(). We know that we can retrieve an item from
a set, and not know what that item will be, but that would not be actually random.

A set is implemented essentially the same as a dict in python, so the time
complexity of add / delete is on average O(1). When it comes to the random
function, however, we run into the problem of needing to convert the data into
a python list in order to return a random element. That conversion will add a
significant overhead to getRandom, thus slowing the whole thing down.

Instead of having to do that type conversion (set to list) we can take an approach
that involves maintaining both a list and a dictionary side by side.


The list is maintained solely for the purpose of returning a random element,
and the dictionary will be used for knowing the index of each element
in the list b)
"""

class RandomizedSet:

    def __init__(self):
        self.data_map = {}
        self.data = []

    def insert(self, val: int) -> bool:
        # lookup in dict is significantly more efficient than in a list
        if val in self.data_map:
            return False
        self.data_map[val] = len(self.data)
        self.data.append(val)
        return True

    def remove(self, val: int) -> bool:
        if not val in self.data_map:
            return False

        # take the postion of the last item in the array and move it to
        # the position of the item to be removed
        self.data_map[self.data[-1]] = self.data_map[val]
        self.data[self.data_map[val]] = self.data[-1]
        self.data[-1] = val
        self.data.pop()
        self.data_map.pop(val)
        return True

    def getRandom(self) -> int:
        return random.choice(self.data)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

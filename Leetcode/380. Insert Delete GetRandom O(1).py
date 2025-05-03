'''
Question: 380. Insert Delete GetRandom O(1)

Implement the RandomizedSet class:

RandomizedSet() Initializes the RandomizedSet object.
bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
You must implement the functions of the class such that each function works in average O(1) time complexity.

'''

'''
Understand the question:

This question is asking you to implement a data structure called RandomizedSet that supports 3 operations:

insert(val)
Adds val to the set if it's not already present.

Returns true if the insertion happened (i.e., the value was not already in the set).

Returns false if the value was already present.

remove(val)
Removes val from the set if it exists.

Returns true if the value was in the set and successfully removed.

Returns false otherwise.

getRandom()
Returns a random element from the current set, with each element having an equal chance of being chosen.

There will always be at least one element in the set when this is called.


'''

'''
Learning:

1. what is data structure?

A data structure is a way of organizing and storing data in a computer so that it can be used efficiently.

Think of it like a toolbox:

Each tool (data structure) is designed for a specific type of job (task).

Some are good for fast searching, others for quick adding/removing, or maintaining order.

Common Types of Data Structures:

| Data Structure            | Description                                       | Example Use                                  |
| ------------------------- | ------------------------------------------------- | -------------------------------------------- |
| **Array / List**          | A collection of elements stored in a fixed order. | Storing a list of numbers or names.          |
| **Hash Map / Dictionary** | A collection of key-value pairs for fast lookup.  | Finding a user's profile by ID.              |
| **Set**                   | A collection of unique items (no duplicates).     | Tracking unique values like email addresses. |
| **Stack**                 | Last-in, first-out (LIFO).                        | Undo feature in apps.                        |
| **Queue**                 | First-in, first-out (FIFO).                       | Printer job queue.                           |
| **Tree**                  | A hierarchical structure.                         | File systems, family trees.                  |
| **Graph**                 | A set of nodes connected by edges.                | Social networks, maps.                       |


2. what is hash map?
In python, a dictionary is essentially a hash map. It allows you to store key-value pairs, where each key is unique and maps to a specific value.

'''


#Solution:

import random

class RandomizedSet:

    def __init__(self):
        self.val_to_index = {}  # maps value to its index in the list
        self.values = []        # list of inserted values

    def insert(self, val: int) -> bool:
        if val in self.val_to_index:
            return False
        self.values.append(val)
        self.val_to_index[val] = len(self.values) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_index:
            return False
        # Get index of the element to remove
        idx_to_remove = self.val_to_index[val]
        last_element = self.values[-1]

        # Move the last element to the place of the element to delete
        self.values[idx_to_remove] = last_element
        self.val_to_index[last_element] = idx_to_remove

        # Remove the last element from the list and delete from dict
        self.values.pop()
        del self.val_to_index[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.values)

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

Dictionary:

In Python, a dictionary is a collection of key-value pairs. You add values to it using this basic syntax:

my_dict[key] = value

i.e.

my_dict = {}  # Start with an empty dictionary

# Add the first key-value pair
my_dict['apple'] = 5

# Add the second key-value pair
my_dict['banana'] = 3


print(my_dict['apple'])
print(my_dict['banana'])


How do I get the key (like 'apple') by using the value 5 in a dictionary?

In Python, dictionaries are designed to look up values by keys, not the other way around.
Banana is the key, and 3 is the value.

So this works:
my_dict = {'apple': 5, 'banana': 3}
print(my_dict['apple'])  # ➜ 5 ✅

But this won't work:

print(my_dict[5])  # ❌ KeyError

🔁 How to "get the key from a value" (e.g., 5 → 'apple')?
You'll need to search through the dictionary manually like this:

for key, value in my_dict.items():
    if value == 5:
        print(key)       # ➜ 'apple' ✅

'''


'''
Let's do some revision on Class:

1. what is __init__ ?

The __init__ method is a special method in Python classes. 
It's called a constructor and is automatically invoked when you create an instance of the class. 
Its primary purpose is to initialize the attributes of the new object.

When You Need __init__:
You need it when you want to set up attributes when an object is created.

i.e. 

class Dog:
    def __init__(self, name):
        self.name = name

d = Dog("Buddy")
print(d.name)  # Buddy


When You Don't Need __init__:
If your class:

Doesn't need any data;

Only contains methods;

Just uses class-level variables;

Then you can skip __init__.

i.e.

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        nums1[:m+n] = nums1[:m] + nums2[:n]
        nums1.sort()

Just like many previous questions where we ignored __init__ method and just created a class with methods.
'''
''''
Random modules:

What is random?
random is a built-in module in Python, which provides a suite of functions for generating random numbers or making random choices.

Purpose of random module: 
It includes functions for generating random numbers (e.g., random.randint()), 
making random choices from a list (e.g., random.choice()), 
and other random operations (like shuffle(), uniform(), etc.).
'''

#Solution:
import random
class RandomizedSet:

    def __init__(self):
        self.dict = {}  # maps value to its index in the list
        self.list = []  # list of inserted values

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        self.dict[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.dict:
            return False
        # Get index of the element to remove
        index_to_remove_in_dict = self.dict[val] # index of the element to remove
        last_element_in_list = self.list[-1] # last element in the list

        # Move the last element to the place of the element to delete
        self.dict[last_element_in_list] = index_to_remove_in_dict # update the index of the last element to the index of the element to remove
        self.list[index_to_remove_in_dict] = last_element_in_list # reassign the last element to the index of the element to remove


        # Remove the last element from the list and delete from dict
        del self.dict[val]
        self.list.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.list)
    

randomizedSet = RandomizedSet()
randomizedSet.insert(1)
randomizedSet.insert(2)
randomizedSet.remove(1)
print(randomizedSet.getRandom())


'''
Explanation of how to use the class:

randomizedSet = RandomizedSet()

You need to create an instance of the RandomizedSet class first.
Then you can call its methods like insert, remove, and getRandom.
Just like an other class we created before.

'''

'''
Why I need to use self.val_to_index but not just val_to_index:


Understanding self in Python:
In Python, self refers to the current instance of the class.

When you define a method inside a class, the first parameter (usually named self) refers to the instance of the class that is calling the method.

Any attribute or method prefixed with self. is a instance variable or instance method, 
which means it belongs to the specific instance of the class and not to the class itself.

Why self.val_to_index is used instead of val_to_index

1. Class Context:
The val_to_index variable is defined as part of the instance of the RandomizedSet class. 
It's used to store the mapping of values to indices for that specific instance.

class RandomizedSet:
    def __init__(self):
        self.val_to_index = {}  # This is an instance variable
        self.values = []        # This is also an instance variable
self.val_to_index is a dictionary that's unique to each instance of RandomizedSet. It keeps track of the values and their indices for that particular object.

2. Accessing Instance Variables:
Inside a method, when you want to access or modify an instance variable (like val_to_index), you need to use self to reference the variable. 
This tells Python that you're working with the instance variable tied to the object calling the method.

Without self, Python would treat val_to_index as a LOCAL VARIABLE that exists only within the scope of the method, and not as part of the class.

If you try to use val_to_index without self, Python will look for a local variable in the method's scope. 
If it doesn't find one, it will raise an error saying the variable is undefined.


def insert(self, val: int) -> bool:
    if val in self.val_to_index:  # Accessing the instance variable using self
        return False
    self.values.append(val)
    self.val_to_index[val] = len(self.values) - 1  # Updating the instance variable
    return True

Why not use just val_to_index?
If you don't use self, Python won't understand that val_to_index is an instance variable, 
and it would assume you're referring to a local variable or something undefined.

Using self ensures that each instance of RandomizedSet has its own val_to_index and maintains its own state.

Example to illustrate:
Let's imagine this example with two instances of RandomizedSet.

class RandomizedSet:
    def __init__(self):
        self.val_to_index = {}  # instance variable
        self.values = []        # instance variable

    def insert(self, val: int) -> bool:
        if val in self.val_to_index:
            return False
        self.values.append(val)
        self.val_to_index[val] = len(self.values) - 1
        return True

set1 = RandomizedSet()
set2 = RandomizedSet()

# Insert values into set1
set1.insert(10)
set1.insert(20)

# Insert values into set2
set2.insert(30)
set2.insert(40)

# Check values
print(set1.val_to_index)  # {10: 0, 20: 1}
print(set2.val_to_index)  # {30: 0, 40: 1}
Here, set1 and set2 are two different instances of RandomizedSet. Each instance has its own val_to_index dictionary.

If you used val_to_index without self, both instances would try to access the same dictionary, 
and they'd overwrite each other's data, which would break the logic of having independent sets.

'''

'''
pop():

The pop() method does two things:

Modifies the list by removing the last element.

Returns the removed value.

nums = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print (nums.pop())
print (nums)

'''


'''
For the remove method:

here is the step-by-step explanation:

self.num = [5, 8, 3, 12, 7, 20, 25, 18, 1, 10]
self.num_to_index = {
    5: 0, 8: 1, 3: 2, 12: 3, 7: 4,
    20: 5, 25: 6, 18: 7, 1: 8, 10: 9
}

If we want to remove 12, we need to do the following:


Step 1: Check if 12 is in the dictionary

if 12 not in self.num_to_index:
    return False
✅ Yes, 12 exists.

Step 2: Get the index of 12

index_to_remove_in_dict = self.num_to_index[12]  # 3

Step 3: Get the last element in the list

last_element_in_list = self.num[-1]  # 10

Step 4: Overwrite the index of 12 with the last element (10)

self.num[3] = 10
List becomes:

self.num = [5, 8, 3, 10, 7, 20, 25, 18, 1, 10]
Now update the dictionary for 10:

self.num_to_index[10] = 3
Dictionary becomes:

{
    5: 0, 8: 1, 3: 2, 12: 3, 7: 4,
    20: 5, 25: 6, 18: 7, 1: 8, 10: 3
}
Notice how 12 is still in the dictionary temporarily.

Step 5: Remove the last element and delete the old mapping

self.num.pop()             # removes the second 10
del self.num_to_index[12]  # clean up
Final list:


self.num = [5, 8, 3, 10, 7, 20, 25, 18, 1]
Final dictionary:


{
    5: 0, 8: 1, 3: 2, 10: 3, 7: 4,
    20: 5, 25: 6, 18: 7, 1: 8
}
✅ 12 has been cleanly removed.

'''


'''
To delete an element from a dictionary in Python, you can use the del statement.
The syntax is as follows:
del dictionary[key]
This will remove the key-value pair associated with the specified key from the dictionary.
For example:

my_dict = {'a': 1, 'b': 2, 'c': 3}
del my_dict['b']
print(my_dict)  # Output: {'a': 1, 'c': 3}

'''


'''
A key point to achieve 0(1) time complexity for insert, remove, and getRandom is:
to use      if val in self.dict:
            return False

to check if the value is already in the dictionary.

rather than if val in self.list:
            return False
This is because checking membership in a dictionary is O(1) on average, while checking membership in a list is O(n).

why?

When you do:

if val in my_dict:

Computes the hash of val (e.g. hash(val)).

Uses that hash to jump directly to the memory location where that value should be.

Checks if the value is present there.

✅ This is extremely fast and doesn’t depend on how big the dictionary is.

❌ Lists: Linear Time — O(n)
When you do:

if val in my_list:
Python has no idea where val might be — lists are ordered sequences, not hashed.

So Python has to:

Start at the first item.

Compare val to each item one-by-one.

Stop if it finds a match or reaches the end.

⏳ This gets slower as the list gets longer.
'''
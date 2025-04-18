'''
Question:
88. Merge Sorted Array
Two integer arrays nums1 and nums2 are given, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
Merge nums1 and nums2 into a single array sorted in non-decreasing order.
The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
To accommodate this, nums1 has a length of m + n, 
where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.


Non-decreasing	a[i] <= a[i+1]
Increasing	a[i] < a[i+1]

✅ Non-decreasing order
Means that the values stay the same or increase — they never go down.

Example:
1, 2, 2, 3, 4

🔼 Increasing order (strictly increasing)
Means that each value must be greater than the one before — no repeats allowed.

Example:
1, 2, 3, 4, 5
------------------------------------------------------------------------------------------------

Notes:
Class is a blueprint for creating objects.
An object is an instance of a class.

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

#Create objects (instances) of the Car class

car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Civic", 2022)

Car is a class that represents a car.
# It has three attributes: make, model, and year.
car1 and car2 are objects (instances) of the Car class.

------------------------------------------------------------------------------------------------

Type hinting is a feature in Python that allows you to specify the expected data types of function arguments and return values.
It helps improve code readability and can assist with static type checking.
It doesn't enforce that type at runtime, but it acts as a guideline or suggestion to the developer.
nums1: list[int]: It tells us that nums1 is expected to be a list, and the type of each element in that list should be int.

However,
nums1 will also work without type hinting, as Python is a dynamically typed language.

hence, 

def merge(self, nums1: list[int], m: int, nums2: list[int], n: int):
is equivalent to:
def merge(self, nums1, m, nums2, n):

-----------------------------------------------------------------------------------------------
-> None

what is -> + xxx i.e -> None or -> int or -> str etc.
-> + xxx is a type hint that indicates the return type of the function.

i.e. 
def add(a: int, b: int) -> int:
    return a + b

This tells us:

a and b are both integers (int)

The function returns an integer (-> int)

Without ->, the function still works, but using it makes your code easier to understand and helps tools like linters or IDEs catch bugs early.
'''

#Solution:

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        # Filter out non-zeroq elements (meaningful data from nums1)
        nums1[:m+n] = nums1[:m] + nums2[:n]
        nums1.sort()

# Test it
sol = Solution()
nums1 = [1, 2, 3, 0, 0, 0] # 0 is a placeholder for the elements of nums2, it is not part of the original nums1 list, hence doesn't violate the non-decreasing order.
m = 3
nums2 = [2, 5, 6]
n = 3
sol.merge(nums1, m, nums2, n)
print(nums1) 

'''
This Question can have multiple variations depending on the request.

Question type 1:
Merge first m elements of nums1 with first n elements of nums2 and sort them in non-decreasing order.
Solution:
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    
        nums1[:m+n] = nums1[:m] + nums2[:n]
        nums1.sort()

Question type 2:
Replace 0s in nums1 with the elements of nums2, provided nums1 has enough space to accommodate them. 
i.e. nums1 has a length of m + n, and has the same number of 0s as the number of elements (n) in nums2.

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        # Filter out non-zero elements (meaningful data from nums1)
        nums1_clean = [x for x in nums1 if x != 0]
        merged = nums1_clean + nums2
        merged.sort()
        nums1[:] = merged

# Test it
sol = Solution()
nums1 = [0, 2, 0, 3, 0, 6]
m = 3
nums2 = [2, 5, 6]
n = 3
sol.merge(nums1, m, nums2, n)
print(nums1)  # ➜ [2, 2, 3, 5, 6, 6]


Question type 3:
Insert nums2 into nums1

class Solution:
    def merge(self, nums1: list[int], nums2: list[int]) -> None:
        nums1 += nums2
        nums1.sort()
# Test it
sol = Solution()
nums1 = [0, 2, 0, 3, 0, 6]
nums2 = [2, 5, 6]
sol.merge(nums1, nums2)
print(nums1)

Question type 4:
Insert n elements from nums2 into nums1 which has m elements, at the start, middle or end of nums1.

class Solution:
    def merge(self, nums1: list[int], nums2: list[int], index:int) -> None:
        nums1[index:index] = nums2 
        #when index = 0, insert at the start of nums1
        #when index = len(nums1), insert at the end of nums1
        #when index = len(nums1)//2, insert at the middle of nums1
        nums1.sort()
# Test it
sol = Solution()
nums1 = [0, 2, 0, 3, 0, 6]
nums2 = [2, 5, 6]
index = 3
sol.merge(nums1, nums2, index)
print(nums1)
'''

'''
nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3

expected output: [1,2,2,3,5,6]

If I do:
        nums1 = nums1 + nums2
        nums1 = [x for x in nums1 if x != 0]
        nums1.sort()
        print(nums1)

        the output will be:
        [1, 2, 2, 3, 5, 6]
        which is correct.
        However, leetcode will not accept this solution because it is not in-place.
        Aka, it is not modifying the original nums1 list.
        Instead, it is creating a new list and assigning it to nums1.

        This satisfies the 'in-place' requirement of the question:
        nums1[0:m+n] = nums1[0:m] + nums2[0:n]
        nums1.sort()

        Why? 
        What is inplace?
        In-place means that the original data structure is modified directly without creating a new copy of it.
        nums1 = ... (which replaces the whole list object).
        nums1[:] = ... (which modifies the contents of the list object in place).
        Especially important in Python when lists are passed by reference. If you do nums1 = something, the original reference is lost. But if you do nums1[:] = something, the original list is updated.

'''


'''
nums = [10, 11, 12, 13, 14]
for i in nums:
    print(i)

output: [10, 11, 12, 13, 14]

vs 

for i in range(len(nums)):
    print(i)
output: [0, 1, 2, 3, 4] #It will print the index of the elements in nums.

vs

for i in range(len(nums)):
    print(nums[i])

output: [10, 11, 12, 13, 14] #It will print the elements in nums.

Hence:
for i in nums:
    print(i)

is the same as 

for i in range(len(nums)):
    print(nums[i])

Despite the fact that work slightly differently, they are functionally equivalent in this case.
However, bear in mind that for i in nums, it is reading the elements of nums directly, while for i in range(len(nums)), 
it is reading the indices of nums and then using those indices to access the elements.

There are cases where you can only use for i in range(len(nums)), for example, if you want to modify the elements of nums in place. (e.g. Question 27. Remove Element)


#enumerate()
This is a built-in function in Python that takes an iterable (like a list)

nums = [10, 11, 12, 13, 14]
print(list(enumerate(nums)))
#output: [(0, 10), (1, 11), (2, 12), (3, 13), (4, 14)]
#It will print the index and the element in nums.
This is a built-in function in Python that takes an iterable (like a list) 
and returns an iterator that produces pairs of an index and the corresponding value from the iterable.

nums = [10, 11, 12, 13, 14]

for index, number in enumerate(nums):
    print([index, number])
#output: [(0, 10), (1, 11), (2, 12), (3, 13), (4, 14)]

'''


'''
TypeError: 'list' object is not callable

This happens when you try to call a list as if it were a function.
i.e print (nums1(2)) instead of print(nums1[2])
# This is a common mistake when using parentheses instead of square brackets to access list elements.
'''
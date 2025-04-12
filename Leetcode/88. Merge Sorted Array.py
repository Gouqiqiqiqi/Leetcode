'''
Question:
88. Merge Sorted Array
Two integer arrays nums1 and nums2 are given, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
Merge nums1 and nums2 into a single array sorted in non-decreasing order.
The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
To accommodate this, nums1 has a length of m + n, 
where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

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
        # Combine the valid elements from nums1 with the elements from nums2.
        nums1 = nums1 + nums2
        # Sort the combined list in place.
        nums1.sort()

sol = Solution()
nums1 = [0, 2, 0, 3, 0, 6]  # nums1 has enough space for nums2
m = 3
nums2 = [2, 5, 6]
n = 3
sol.merge(nums1, m, nums2, n)
print(nums1) 

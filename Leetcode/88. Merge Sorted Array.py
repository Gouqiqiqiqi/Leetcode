'''
Question:
88. Merge Sorted Array
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, 
representing the number of elements in nums1 and nums2 respectively.
Merge nums1 and nums2 into a single array sorted in non-decreasing order.
The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
To accommodate this, nums1 has a length of m + n, 
where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.


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
        # Start from the end of both arrays
        p1 = m - 1  # last index of initial nums1
        p2 = n - 1  # last index of nums2
        p = m + n - 1  # last index of nums1

        # Merge in reverse
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        # Fill in the rest of nums2 (if any left)
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1

sol = Solution()
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
sol.merge(nums1, m, nums2, n)
print(nums1)  # Output: [1, 2, 2, 3, 5, 6]

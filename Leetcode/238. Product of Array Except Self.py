'''
Question: 238. Product of Array Except Self
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
'''

#Solution:

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        answer = [1] * n # This will create a list with n elements, all initialized to 1.

        # Calculate prefix products
        prefix_product = 1 #We haven't encountered any elements yet, so the prefix product is 1; Why 1? Again, because 1 is the multiplicative identity.
        for i in range(n):
            answer[i] = prefix_product
            prefix_product *= nums[i]

        # Calculate suffix products and multiply with prefix products
        suffix_product = 1 # We haven't encountered any elements yet, so the suffix product is 1; Why 1? Again, because 1 is the multiplicative identity.
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix_product # Multiply prefix product with suffix product
            suffix_product *= nums[i]

        return answer


'''
Code Explanation:

answer = [1] * n # This will create a list with n elements, all initialized to 1.
We do this so that we can return the answer with n elements in the end.
Why do we use [1] * n rather than [0] * n?
Because:
[1] is the multiplicative identity, so multiplying by 1 does not change the value.
Since 1 X anything = anything, we can use [1] * n to initialize our answer array.

[0] is the additive identity, so adding 0 does not change the value.
As 0 + anything = anything.
If we use [0] * n to initialize our answer array, then the final answer will be all 0s.
'''


'''
The core logic of the solution is to divide the multiplication into two parts:
1. Calculate the prefix products.
2. Calculate the suffix products and multiply with the prefix products.

For example:
If you have an array of 5 numbers:
nums = [a, b, c, d, e]

The product of all numbers is:
a × b × c × d × e

But if you want the product excluding index i (say i = 2, which is c),
you multiply everything except c:
a × b × d × e

Therefore we create two parts of the product, one before the index (prefix_product) and one after the index (suffix_product).

'''

'''
Note about for i in range loop:
for i in range(n):
vs
for i in range(n - 1, -1, -1):

for i in range(n) will iterate from 0 to n-1, where n is the length of the array. Python defaults loop to have a step size of +1.
for i in range(n - 1, -1, -1) will iterate from n-1 to 0, where n is the length of the array. The step size is -1.
1. n - 1 is the last index of the array
2. -1 in the middle is the first index of the array, 
3. -1 in the last means that we have a step size of -1, meaning we are going backwards.
'''

'''
Nums = [3, 4, 5, 6]
This might be difficult to understand at first, but this:

prefix_product = 1
for i in range(n):
    answer[i] = prefix_product
    prefix_product *= nums[i]

Will give you the prefix product of all elements before index i.
For example:

| Index i   | nums[i]  | Prefix Product (Before i)   | Product of All Elements Before i |
| --------- | -------- | --------------------------- | ---------------------------------|
| 0         | 3        | 1                           | No elements before → 1           |
| 1         | 4        | 3                           | Product of [3] → 3               |
| 2         | 5        | 12                          | Product of [3, 4] → 12           |
| 3         | 6        | 60                          | Product of [3, 4, 5] → 60        |

'''
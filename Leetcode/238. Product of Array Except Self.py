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
Let's understand the question first:

So basically if given an array of [2,3,4,5]

The calculation will be [3x4x5, 2x4x5, 2x3x5, 2x3x4]

answer[0] = 3 × 4 × 5 = 60
answer[1] = 2 × 4 × 5 = 40
answer[2] = 2 × 3 × 5 = 30
answer[3] = 2 × 3 × 4 = 24

So the output will be [60, 40, 30, 24]

Now a key concept to solve the problem is:

Total product except nums[i] = product of all elements before i × product of all elements after i

If we think about it, use num[0] as an example:
The product of all elements before index 0 is 1 (since there are no elements before it).
The product of all elements after index 0 is 3 × 4 × 5 = 60.
So answer[0] = 1 × 60 = 60.
And so on for the other indices.

So the question now becomes how do we use codes to calculate the product of all elements before and after each index?


nums = [2, 3, 4, 5]


Prefix products:

prefix = 1
for i in range(n):
    answer[i] = prefix        # step 1:assign product so far
    prefix *= nums[i]         # step 2:update prefix for next step

The key is to assign answer[i] = prefix before updating prefix, 
so that answer[i] contains the product of all elements before index i.

i = 0 → answer[0] = 1 (no numbers before), prefix = 1×2 = 2

i = 1 → answer[1] = 2, prefix = 2×3 = 6

i = 2 → answer[2] = 6, prefix = 6×4 = 24

i = 3 → answer[3] = 24, prefix = 24×5 = 120

Suffix products:

suffix = 1
for i in range(n - 1, -1, -1):
    answer[i] *= suffix      # multiply by suffix so far
    suffix *= nums[i]        # update suffix for next step

i = 3 →  suffix = 1×5 = 5, answer[3] = 24 × 1 = 24

i = 2 → suffix = 5×4 = 20, answer[2] = 6 × 5 = 30

i = 1 → suffix = 20×3 = 60, answer[1] = 2 × 20 = 40

i = 0 → suffix = 60×2 = 120, answer[0] = 1 × 60 = 60

answer = [60, 40, 30, 24]


Now, another key insight is that why answer[i] = prefix doesn't include nums[i]?

Because  we are always "one step behind"

Let’s walk through an example with nums = [2, 3, 4, 5]:

prefix = 1
answer = [1, 1, 1, 1]

for i in range(n):
    answer[i] = prefix
    prefix *= nums[i]

'''






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
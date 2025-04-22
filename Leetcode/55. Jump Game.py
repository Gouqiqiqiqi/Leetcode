'''
You are given an integer array nums. 
You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.
'''

'''
This question is a classic example of the greedy algorithm.
nums = [2, 3, 1, 1, 4]
output = True
Question explanation: 
First number is 2 so you can jump 1 or 2 steps forward.
Jumping 1 step forwards to 3 is the best option because it allows you to jump 2 steps forward to 4, which is the end of the array. Problem solved.
'''

# To solve this problem, we only care if we can reach the current index using the maximum jump length.
# And we loop through the array, if we can always reach the current index, we can reach the last index.

class Solution:
    def canJump(self, nums: list[int]) -> bool:
        farthest_index = 0
        for i in range(len(nums)):
            if i > farthest_index:
                return False
            farthest_index = max(farthest_index, i + nums[i])
        return True
    

s = Solution()
nums = [2, 3, 1, 1, 4]
print(s.canJump(nums))  # Output: True


'''
# Logic of thoughts:
1. Given an array of integers, we need to check if we can reach the last index from the first index.
2. I care about the furthust index I can reach from the starting index. 
3. As long as the furthest index equals or exceeds the last index, I can reach the last index.
4. farthest_index = 0, this variable will keep track of the farthest index we can reach so far. 
5. i.e. If length of an array is 5 (1, 2, 3, 4, 5), as long as farthest_index is greater or equal to 4, we can reach the last index, vice versa.
6. The algorithm iterates through the array, updating the farthest index reachable at each step.
'''


'''
Line by line explaination:

farthest_index  = 0
# This keeps track of the farthest index you can reach so far.
# If a nums list has 5 elements, farthest_index needs to be 4 or greater in order to reach the last index.
# At the start, you haven't made any jumps yet, so farthest_index starts as 0.

nums = [2, 3, 1, 1, 4]

for i in range(len(nums)):
    if i > farthest_index:
        return False
    farthest_index = max(farthest_index, i + nums[i])
return True

farthest_index = max(farthest_index, i + nums[i])
# This line updates the farthest index reachable at each step.
# i + nums[i] is the farthest index reachable from the current index.
# if i = 0, nums[i] = 2, then i + nums[i] = 2, so farthest_index = max(0, 2) = 2.
# if i = 1, nums[i] = 3, then i + nums[i] = 4, so farthest_index = max(2, 4) = 4.


The loop is checking whether fartest_index is greater than or equal to the current index.
# If it is, we can reach that index. If it isn't, we can't reach that index and return False.
# If we reach the end of the loop without returning False, it means we can reach the last index, so we return True.

if i > farthest_index:

    If i is greater than the farthest index we could reach so far, then we're stuck — we hit a point we cannot jump to.

    So, return False.

farthest_index = max(farthest_index, i + nums[i])

    If we are not stuck, we update farthest_index to the furthest we can go from current index i.

    i + nums[i] is the max position we can jump to from index i.

    So this step says: "Can we go even further from here?"

'''


'''
nums = [2, 3, 1, 1, 4]

farthest = 0

farthest = max(farthest, nums[i] + i)

print ([nums[i] + i for i in range (len(nums))])

#Output is [2, 4, 3, 4, 8]

This means 

nums[0] = 2 can reach index 2

nums[1] = 4 can reach index 4 --Already reached last index

nums[2] = 3 can reach index 3 

nums[3] = 4 can reach index 4 

nums[4] = 4 can reach index 8 
'''
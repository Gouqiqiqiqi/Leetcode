'''
Question: Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. 
In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9

'''

#This question is hard, prefix_suffix method is eaiser to understand, but two pointers is more efficient.

#Prefix/Suffix Arrays
class Solution:
    def trap(self, height: list[int]) -> int:
        left_wall = 0
        right_wall = 0
        n = len(height)
        max_left = [0] * n
        max_right = [0] * n

        for i in range(n):
            j = -i - 1
            max_left[i] = left_wall
            left_wall = max(left_wall, height[i])
            max_right[j] = right_wall
            right_wall = max(right_wall, height[j])

        water = 0
        for i in range(n):
            pot = min(max_left[i], max_right[i])
            water += max(0, pot - height[i])

        return water

'''
The logic for the prefix/suffix method is as follows:
for a given array of heights, we need to find the maximum height to the left and right of each bar.
We can do this by creating two arrays, max_left and max_right, where:
- max_left[i] is the maximum height to the left of index i (including index i itself)
- max_right[i] is the maximum height to the right of index i (including index i itself)

The trick to solve this problem is to realize that the amount of water that can be trapped above each bar 
is determined by the minimum of the maximum heights to its left and right at that bar (i), 
minus the height of the bar itself.


For example,

given the height array [0,1,0,2,1,0,1,3,2,1,2,1], 

max_left would be:
[0, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3]
max_right would be:
[3, 3, 3, 3, 3, 3, 2, 2, 1, 1, 1, 1]

min(max_left[i], max_right[i]) is 
[0, 1, 1, 2, 2, 2, 2, 3, 2, 1, 1, 1],
which gives us the potential water level above each bar.

Then for each index i, the water trapped above that bar is:

max(0, min(max_left[i], max_right[i]) - height[i]) is 
[0, 0, 1, 0, 1, 2, 1, 0, 0, 0, 1, 0]

So the total water trapped is 6.

'''

'''
A note to myself, i made this mistake in the first attempt:

I used 

max_left = max_right = [0] * n 

instead of

max_left = [0] * n
max_right = [0] * n


This leads to failure.

The reason is because this line creates a single list in memory and assigns it to both max_left and max_right. 
So any change I make to one will affect the other, because they are references to the same object.


Example of the problem:
a = b = [0] * 3
a[0] = 5
print(b)  # Output: [5, 0, 0]  — b is changed too!



In contrast:
max_left = [0] * n
max_right = [0] * n
This creates two separate lists, which is what I want.
One to store the max height to the left of each bar, and one to store the max height to the right.
'''



#Two Pointers
class Solution:
    def trap(self, height: list[int]) -> int:
        if not height:
            return 0
        
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        water = 0

        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                water += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                water += right_max - height[right]

        return water


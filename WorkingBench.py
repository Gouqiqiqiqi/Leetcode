class Solution:
    def removeElementAndReturnArray(self, nums: list[int], val: int) -> int:
        k = 0  # Number of elements not equal to val
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        # Trim the original list to only include the first k elements
        del nums[k:]
        return k  # Optionally return k if needed

# Example usage
nums = [3, 2, 2, 3, 3]
val = 2
sol = Solution()
k = sol.removeElementAndReturnArray(nums, val)

print(k)
print(nums)
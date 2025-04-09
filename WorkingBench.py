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
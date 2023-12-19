def merge(nums1, m, nums2, n):
    # Initialize pointers for nums1 and nums2 and the merged array index
    p1 = m - 1
    p2 = n - 1
    p_merged = m + n - 1

    # Merge nums1 and nums2 from the end to the beginning
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p_merged] = nums1[p1]
            p1 -= 1
        else:
            nums1[p_merged] = nums2[p2]
            p2 -= 1
        p_merged -= 1

    # If there are remaining elements in nums2, copy them to nums1
    while p2 >= 0:
        nums1[p_merged] = nums2[p2]
        p2 -= 1
        p_merged -= 1

# Example usage:
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

merge(nums1, m, nums2, n)
print(nums1)
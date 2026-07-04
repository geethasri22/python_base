#Dutch National Flag
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # Three pointers: low for 0, mid for 1, high for 2
        n = len(nums)
        low, mid, high = 0, 0, n-1
        while mid <= high:
            if nums[mid] == 0:# Swap current with low, move both forward
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:# Leave 1 in place, just move mid
                mid += 1
            else:# nums[mid] == 2
                # Swap current with high, move high backward
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1

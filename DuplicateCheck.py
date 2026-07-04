class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n == 0:
            return False   
        if n == 1:
            return False   
        nums.sort()
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False

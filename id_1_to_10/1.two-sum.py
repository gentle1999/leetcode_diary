# use hash map to change space for time
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index_map = dict()
        for i in range(len(nums)):
            diff = target - nums[i]
            try:
                return [index_map[diff], i]
            except:
                index_map[nums[i]] = i

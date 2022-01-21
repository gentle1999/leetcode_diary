# merge sort
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        l1 = len(nums1)
        l2 = len(nums2)
        l_mid, flag = divmod(l1 + l2, 2)
        result = []
        left = nums1
        right = nums2
        while left and right:
            if len(result) > l_mid:
                break
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        while left:
            if len(result) > l_mid:
                break
            result.append(left.pop(0))
        while right:
            if len(result) > l_mid:
                break
            result.append(right.pop(0))
        if flag:
            return result[-1]
        else:
            return (result[-2]+result[-1])/2

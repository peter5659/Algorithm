
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = nums1+nums2
        nums.sort()
        print(nums)
        if len(nums)%2==1:
            return nums[len(nums)//2]
        else: 
            return (nums[len(nums)//2-1]+nums[len(nums)//2])/2.0
        
s = Solution()
nums1 = [1,3]
nums2 = [2]
value = s.findMedianSortedArrays(nums1,nums2)
print(value)
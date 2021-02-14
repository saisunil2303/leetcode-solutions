class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0 
        while ( i < len(nums1) ):
            if ( i < m ):
                i = i + 1
            elif ( j < n ):
                nums1[i] = nums2[j]
                j = j + 1
                i = i + 1
        print (nums1.sort())

"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

The solution below is O(n) but it got accepted.
Can be optimised to O(log (m+n))
"""

def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a = 0
        b = 0
        merger = []
        while a<len(nums1) and b<len(nums2):
            if nums1[a]<=nums2[b]:
                merger.append(nums1[a])
                a+=1
            else:
                merger.append(nums2[b])
                b+=1
        print(merger)
        if a<len(nums1):
            merger.extend(nums1[a:])
        elif b<len(nums2):
            merger.extend(nums2[b:])
        print(merger)
        mid = len(merger)//2
        if len(merger)%2==0:
            median = (merger[mid]+merger[mid-1])/2.
        elif len(merger)%2!=0:
            median = merger[mid]
            
        return median

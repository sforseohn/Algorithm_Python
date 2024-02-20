# Intersection of Two Arrays
class Solution(object):
    def intersection(self, nums1, nums2):
        nums2.sort()
        ans = []

        for n in nums1:
            start, end = 0, len(nums2) - 1

            while start <= end:
                mid = (start + end) // 2
        
                if nums2[mid] < n:
                    start = mid + 1
                elif nums2[mid] > n: 
                    end = mid - 1
                else:
                    ans.append(n)
                    break
        return set(ans)
                
        
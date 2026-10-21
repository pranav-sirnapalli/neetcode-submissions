class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)


        res1 = set1 - set2
        res1_arr = []
        for i in res1:
            res1_arr.append(i)
        #print(res1_arr)

        res2 = set2 - set1
        res2_arr = []
        for i in res2:
            res2_arr.append(i)
        #print(res2_arr)
        return [res1_arr, res2_arr]
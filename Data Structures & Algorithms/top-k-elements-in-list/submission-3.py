class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_track = {}
        res = []

        for i in nums:
            if i in count_track:
                count_track[i] += 1
            else:
                count_track[i] = 1
        
        sorted_count_track = sorted(count_track.items(), key= lambda item: item[1], reverse=True)
        for key, value in sorted_count_track:
            res.append(key)
            k -= 1
            if k == 0:
                break
        return res
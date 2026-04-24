class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        found = 1
        for s1 in strs:
            if len(res) == 0:
                res.append([s1])
            else:
                for i in range(len(res)):
                    if sorted(list(res[i][0])) == sorted(list(s1)):
                        res[i].append(s1)
                        found = 0
                if found:
                    res.append([s1])
                else:
                    found = 1
        return res
                
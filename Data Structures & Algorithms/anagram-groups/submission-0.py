class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        vals = {}
        finallist = []
        seen = [False] * len(strs)
        for s in strs:
            vals[s] = Counter(s)
        
        for i in range(len(strs)):
            if seen[i]: continue
            locallist = [strs[i]]
            seen[i] = True
            for j in range(i+1, len(strs)):
                if not seen[j] and vals[strs[i]] == vals[strs[j]]:
                    locallist.append(strs[j])
                    seen[j] = True
            finallist.append(locallist)

        return finallist
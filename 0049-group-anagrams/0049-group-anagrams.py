class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        data: dict = collections.defaultdict(list)
        for s in strs:
            data["".join(sorted(s))].append(s)
        print(data)
        return list(data.values())
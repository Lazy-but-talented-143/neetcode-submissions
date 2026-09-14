class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anag_g={}
        for word in strs:
            key="".join(sorted(word))
            if key not in anag_g:
                anag_g[key]=[]
            anag_g[key].append(word)
        return list(anag_g.values())
        
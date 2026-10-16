class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen=set()
        for ch in nums:
            if ch not in seen:
                seen.add(ch)
            else:
                return ch
            
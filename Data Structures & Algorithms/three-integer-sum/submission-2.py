class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        s1=[]
        seen=set()
        nums.sort()
        for i in range(len(nums)):
            l=i+1
            r=len(nums)-1
            while l<r:
                s = nums[i] + nums[l] + nums[r]
                if s==0 :
                    t=(nums[i],nums[l],nums[r])
                    if t not in seen:
                        seen.add(t) 
                        s1.append(list(t))
                    l=l+1
                    r=r-1
                elif s < 0:
                    l += 1
                else:
                    r -= 1
        return s1

        
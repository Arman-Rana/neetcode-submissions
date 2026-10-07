class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset=set(nums)

        le=0
        for n in numset:
            if (n-1) not in numset:
                length=1
                while(n+length) in numset:
                    length+=1
                le= max(length,le)
        return (le)
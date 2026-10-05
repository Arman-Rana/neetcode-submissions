class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashsetu={}
        for char in nums:
            hashsetu[char]= hashsetu.get(char,0)+1

        twith=sorted(hashsetu,key=hashsetu.get,reverse=True)[:k]
        return (twith)

        
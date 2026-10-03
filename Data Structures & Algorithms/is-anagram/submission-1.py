class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        count={}
        #counting cgaracter in the string
        for char in s:
            count[char]=count.get(char,0)+1
        #subrtractinf using the t string

        for char in t:
            if char not in count or count[char]==0:
                return False
            count[char]-=1
        return True

            
        
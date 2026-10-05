class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ''
        for s in strs:
            ans += str(len(s)) + '|'  # Adds length + pipe delimiter
            ans += s  # Adds the actual word
        return ans

    def decode(self, s: str) -> List[str]:
        ans=[]
        i,j=0,0
    
        while i<len(s):
            while s[j] != '|':
                j+=1
            wordlen= int(s[i:j])
            ans.append(s[j+1:j+1+wordlen])
            i= j= j+1+wordlen
        return (ans)

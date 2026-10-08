class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        word = strs[0]
        res = ""

        for i in range(len(word)):      #first words len
            for w in strs[1:]:          #on arr's every elements 1 to n
            
                if i >= len(w) or word[i] != w[i]:
                    return res
            
            res += word[i]
        
        return res
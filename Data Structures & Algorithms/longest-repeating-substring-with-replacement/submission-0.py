class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        maxf = 0 # for char
        count = {} 
        result = 0 # for ans, window length 

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1

            #max frequent element Eg. " AABA "
            maxf = max(maxf, count[s[r]])

            #window length  - freq element (3 - 0 + 1) - 3 > 1
            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1    #remove that element and move left by one
                l += 1
            result = max(result, r - l + 1)
        
        return result             
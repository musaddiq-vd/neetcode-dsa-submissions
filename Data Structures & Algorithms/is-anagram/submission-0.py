class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        dict_s = {}
        dict_t = {}

        for num in s:
            dict_s[num] = dict_s.get(num, 0) +1

        for num in t:
            dict_t[num] = dict_t.get(num, 0) +1
        
        return dict_s == dict_t
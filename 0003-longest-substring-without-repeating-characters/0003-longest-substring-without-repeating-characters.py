class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sett = set()
        l = 0
        ans = 0
        for i in range(len(s)) :
            if (s[i] not in sett) :
                sett.add(s[i])
            else :
                while s[i] in sett : 
                    sett.remove(s[l])
                    l += 1
                sett.add(s[i])
            ans = max(ans , i - l + 1)

        return ans
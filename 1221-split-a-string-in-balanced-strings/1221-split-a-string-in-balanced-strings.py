class Solution:
    def balancedStringSplit(self, s: str) -> int:
        l = 0
        ans = 0
        for i in range(len(s)) :
            a = s[l : i + 1]
            if ((i-l + 1) % 2 == 0 and (a.count("R") == a.count("L"))) :
                ans += 1
                l = i+1
        return ans
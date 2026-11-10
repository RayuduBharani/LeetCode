class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        if (len(g) == 0 or len(s) == 0) :
            return 0
        g.sort()
        s.sort()
        

        count = 0
        l = 0
        r = 0

        while l < len(g) and r < len(s):
            if s[r] >= g[l]:
                count += 1
                l += 1
                r += 1
            else:
                r += 1

        return count
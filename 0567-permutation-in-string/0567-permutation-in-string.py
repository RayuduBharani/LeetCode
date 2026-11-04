class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def fun(dicci1 , dicci2) :
            if (len(dicci1) != len(dicci2)) :
                return False
            for i in dicci1 :
                if (i not in dicci2) :
                    return False
                if (dicci1[i] != dicci2[i]) :
                    return False
            return True

        def dicci(s) :
            dicci = {}
            for i in range(len(s)) :
                if (s[i] in dicci) :
                    dicci[s[i]] += 1
                else :
                    dicci[s[i]] = 1
            
            return dicci
        
        k = len(s1)
        l = 0
        dicci1 = dicci(s1)
        dicci2 = {}

        for i in range(len(s2)) :
            if s2[i] in dicci2 :
                dicci2[s2[i]] += 1
            else :
                dicci2[s2[i]] = 1
            
            if (i - l + 1 > k) :
                dicci2[s2[l]] -= 1
                if (dicci2[s2[l]] == 0) :
                    del dicci2[s2[l]]
                l += 1
            if (i - l + 1 == k) :
                if (fun(dicci1 , dicci2) == True) :
                    return True
        
        return False
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def fun(s , k , char) :
            l = 0
            count = 0
            ans = 0
            for i in range(len(s)) :
                if (s[i] == char) :
                    count += 1
                
                while (i - l + 1) - count > k:
                    if (s[l] == char) :
                        count -= 1
                    l += 1
                
                ans = max(ans , i - l + 1)
            return ans

        maxx = 0
        for i in range(65 , 91) :
            print(fun(s , k , chr(i)))
            maxx = max(maxx , fun(s , k , chr(i)))
        return maxx
class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = len(s)
        hm = {}
        hm2 = {}
        j = 0
        ans = 0
        out = s[0]
        for i in range(l):
            try:
                hm2[s[i]] = hm[s[i]]
                hm[s[i]] = i
            except:
                pass
            try:
                if ans < hm[s[i]] - hm2[s[i]] + 1:
                    ans = hm[s[i]] - hm2[s[i]] + 1
                    out = s[hm2[s[i]]:hm[s[i]]+1]
            except:
                pass
            hm[s[i]] = i
            
        return out

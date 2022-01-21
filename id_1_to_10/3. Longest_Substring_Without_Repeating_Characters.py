class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = len(s)
        hm = {}
        j = 0
        ans = 0
        for i in range(l):
            if s[i] in hm:
                # keep the index of char max
                j = max(hm[s[i]], j)
            ans = max(ans, i - j + 1)
            hm[s[i]] = i + 1
        return ans

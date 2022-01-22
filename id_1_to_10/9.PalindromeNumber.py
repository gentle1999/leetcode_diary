class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        j = len(s) - 1
        i = 0 
        while i < j and s[i] == s[j]:
            i += 1
            j -= 1
        if i < j:
            return False
        else:
            return True

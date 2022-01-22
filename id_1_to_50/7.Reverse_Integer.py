class Solution:
    def reverse(self, x: int) -> int:
        flag = 1
        if x < 0:
            flag = -1
            x = str(-x)
        else:
            x = str(x)
        ans = flag*int(x[::-1])
        if ans > 2**31-1 or ans < -2**31:
            return 0
        else:
            return ans

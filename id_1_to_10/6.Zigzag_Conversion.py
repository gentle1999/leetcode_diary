class Solution:
    def convert(self, s: str, numRows: int) -> str:
        l = len(s)
        ans = []
        index = 0
        if numRows == 1:
            return s
        while index < l:
            ans.append(s[index])
            index += (numRows - 1) * 2
        for i in range(1, numRows - 1):
            index = i
            while index < l:
                ans.append(s[index])
                index += (numRows - i - 1) * 2
                try:
                    ans.append(s[index])
                    index += i * 2
                except:
                    pass
        if numRows > 1:
            index = numRows - 1
            while index < l:
                ans.append(s[index])
                index += (numRows - 1) * 2
        return ''.join(ans)

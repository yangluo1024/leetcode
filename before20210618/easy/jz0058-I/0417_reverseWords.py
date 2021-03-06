class Solution:
    def reverseWords(self, s):
        if not s: return s
        s, res = s.strip(), []
        i = j = len(s) - 1
        while i >= 0:
            while i >= 0 and s[i] != ' ': i -= 1
            res.append(s[i+1:j+1])
            while s[i] == ' ': i -= 1
            j = i
        return ' '.join(res)


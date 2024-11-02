class Solution:
    def pal(self, p):
        if p=="":
            return 0
        if p[0]!=p[-1]:
            return 1
        return self.pal(p[1:-1])
    def longestPalindrome(self, s: str) -> str:
        k = ""
        m = 0
        for i in range(len(s)):
            for j in range(len(s), i, -1):
                if len(s[i:j])>m:
                    if self.pal(s[i:j])==0:
                        k = s[i:j]
                        m = len(s[i:j])
        return k

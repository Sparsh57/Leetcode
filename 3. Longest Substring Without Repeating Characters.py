class Solution:
    def check_longest(self, st, start, last):
        unique_chars = set()
        for i in range(start, last):
            if st[i] in unique_chars:
                return i - start  
            unique_chars.add(st[i])
        return last - start 

    def lengthOfLongestSubstring(self, s: str) -> int:
        self.m = 0
        n = len(s)
        for i in range(n):
            if self.m < n - i:
                current_length = self.check_longest(s, i, n)
                self.m = max(self.m, current_length)
        return self.m

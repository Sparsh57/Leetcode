class Solution:
    def reverseWords(self, s: str) -> str:
        lis = s.rstrip().lstrip().split()
        lis = lis[::-1]
        return ' '.join(lis)

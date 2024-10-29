class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1 = len(word1)
        len2 = len(word2)
        k = []
        for i in range(max(len1, len2)):
            if i<len1:
                k.append(word1[i])
            if i<len2:
                k.append(word2[i])
        return ''.join(k)

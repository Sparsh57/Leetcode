class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashmap_str1 = {}
        hashmap_str2 = {}
        for i in range(len(s)):
            if s[i] in hashmap_str1:
                hashmap_str1[s[i]].append(i)
            else:
                hashmap_str1[s[i]] = [i]
            if t[i] in hashmap_str2:
                hashmap_str2[t[i]].append(i)
            else:
                hashmap_str2[t[i]] = [i]
        print(hashmap_str1.values())
        print(hashmap_str2.values())
        if list(hashmap_str1.values())==list(hashmap_str2.values()):
            return True 
        else:
            return False

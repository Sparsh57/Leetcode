class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        gcd = ""
        n1, n2 = len(str1), len(str2)
        for i in range(min(n1, n2)):
            if n2%(i+1)==0 and n1%(i+1)==0:
                substring = str1[:i+1]
                if str2.replace(substring, "") == str1.replace(substring, "") == "":
                    if len(substring)>len(gcd):
                        gcd = substring
        return gcd

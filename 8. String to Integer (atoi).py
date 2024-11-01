class Solution:
    def myAtoi(self, s: str) -> int:
        hash_map = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9}
        copy_s = s.lstrip().rstrip()
        num = 0
        sign = 1
        if copy_s=="":
            return 0
        if copy_s[0]=="+":
            sign = 1
            copy_s = copy_s[1:]
        elif copy_s[0]=="-":
            sign = -1
            copy_s = copy_s[1:]
        while copy_s:
            try:
                if num==0 and copy_s[0]=="0":
                    pass
                else:
                    num = num*10 + hash_map[copy_s[0]]
                copy_s = copy_s[1:]
            except:
                break
        num*=sign
        if num>(2**31-1):
            return 2**31-1
        if num<(-2**31):
            return -2**31
        return num

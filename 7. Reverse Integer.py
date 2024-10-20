class Solution:
    def reverse(self, x: int) -> int:
        num = str(abs(x))[::-1]
        num = int(num)
        if x<0:
            num=-num
        p = 2**31
        if num>(p-1) or num<-p:
            return 0
        return num

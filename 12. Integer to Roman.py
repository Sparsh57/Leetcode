class Solution:
    def char_to_num(self, c, num, s_val, n_high):
        if num // s_val <= 3:
            return c * (num // s_val)
        else:
            return c + n_high

    def intToRoman(self, num: int) -> str:
        fin = ""
        while num != 0:
            if num >= 1000:
                fin += (num // 1000) * "M"
                num %= 1000
            elif num >= 900:
                fin += "CM"
                num -= 900
            elif num >= 500:
                fin += "D"
                num %= 500
            elif num >= 400:
                fin += "CD"
                num -= 400
            elif num >= 100:
                fin += self.char_to_num("C", num, 100, "D")
                num %= 100
            elif num >= 90:
                fin += "XC"
                num -= 90
            elif num >= 50:
                fin += "L"
                num %= 50
            elif num >= 40:
                fin += "XL"
                num -= 40
            elif num >= 10:
                fin += self.char_to_num("X", num, 10, "L")
                num %= 10
            elif num >= 9:
                fin += "IX"
                num -= 9
            elif num >= 5:
                fin += "V"
                num %= 5
            elif num >= 4:
                fin += "IV"
                num -= 4
            else:
                fin += self.char_to_num("I", num, 1, "V")
                num %= 1
        return fin

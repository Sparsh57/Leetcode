class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31

        negative = (dividend < 0) != (divisor < 0)
        
        dividend, divisor = abs(dividend), abs(divisor)
        
        quotient = 0
        while dividend >= divisor:
            temp_divisor, multiple = divisor, 1
            while dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                multiple <<= 1
            dividend -= temp_divisor
            quotient += multiple
        
        quotient = -quotient if negative else quotient
        
        return max(MIN_INT, min(MAX_INT, quotient))

from itertools import product
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone_dict = {'2':["a", "b", "c"], '3':["d", 'e', 'f'], '4':['g', 'h', 'i'], '5':['j', 'k', 'l'], '6':["m", "n", "o"], '7':['p', 'q', 'r', 's'], '8':['t', 'u', 'v'], '9':['w', 'x', 'y', 'z']}
        a = []
        while digits:
            a.append(phone_dict[digits[0]])
            digits = digits[1:]
        c = []
        if a!=[]:
            for i in list(product(*a)):
                c.append(''.join(i))
        return c

from fractions import Fraction

class Solution:
    def fractionAddition(self, exp: str) -> str:
        e = eval(exp)
        s = str(e).split('.')[1]
        l = str(e).split('.')[0]

        if isinstance(e, float) and s == '0':
            return str(l) + '/1'

        
        ll = str(e)
        f = Fraction(ll).limit_denominator(10000000000)

        return str(f)

    

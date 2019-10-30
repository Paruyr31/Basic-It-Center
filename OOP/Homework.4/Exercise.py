class Fraction():
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        self.fraction = self.numerator / self.denominator
    def __eq__(self, other):
        return self.fraction == other.fraction
    def __ne__(self, other):
        return self.fraction != other.fraction
    def __lt__(self, other):
        return self.fraction < other.fraction
    def __gt__(self, other):
        return self.fraction > other.fraction
    def reduction(self):
        b_den = 0
        nm = self.numerator
        dn = self.denominator
        m = max(nm, dn)
        for i in range(1, m+1):
            if nm % i == 0 and dn % i == 0:
                b_den = i
        if b_den == 1:
            print(str(int(nm))+"/"+str(int(dn)))
        else:
            nm /= b_den
            dn /= b_den
            print(str(int(nm))+"/"+str(int(dn)))
    def __add__(self, other):
        b_den = 0
        m = max(self.denominator, other.denominator)
        for i in range(1, m+1):
            if self.denominator % i == 0 and other.denominator % i == 0:
                b_den = i
        if b_den == 1:
            b_den = self.denominator*other.denominator
        nm = int(b_den/self.denominator*self.numerator + b_den/other.denominator*other.numerator)
        return Fraction(nm, b_den)
    def __sub__(self, other):
        b_den = 0
        m = max(self.denominator, other.denominator)
        for i in range(1, m+1):
            if self.denominator % i == 0 and other.denominator % i == 0:
                b_den = i
        if b_den == 1:
            b_den = self.denominator*other.denominator
        nm = int(b_den/self.denominator*self.numerator - b_den/other.denominator*other.numerator)
        return Fraction(nm, b_den)
    def __mul__(self, other):
        nm = self.numerator*other.numerator
        dn = self.denominator*other.denominator
        return Fraction(nm, dn)
    def __truediv__(self, other):
        nm = self.numerator*other.denominator
        dn = self.denominator*other.numerator
        return Fraction(nm, dn)
    def __mod__(self, other):
        b_den = 0
        m = max(self.denominator, other.denominator)
        for i in range(1, m+1):
            if self.denominator % i == 0 and other.denominator % i == 0:
                b_den = i
        if b_den == 1:
            b_den = self.denominator*other.denominator
        f1 = self.numerator / self.denominator
        f2 = other.numerator / other.denominator
        nm = other.numerator
        if f1/f2 >= 1:
            div = f1//f2
            nm *= div
        sb = int(b_den/self.denominator*self.numerator - b_den/other.denominator*nm)
        return Fraction(sb, b_den)

fr1 = Fraction(3, 4)
fr2 = Fraction(2, 4)
(fr1+fr2).reduction()
import fractions


class Fraction:
    
    def __init__(self, num, denom):
        self._numerator = 0
        self._denominator = 0
        self.numerator = num
        self.denominator = denom
    
    @property
    def numerator(self):
        return self._numerator
    
    @numerator.setter
    def numerator(self, num):
        self._numerator = num
        
    @property
    def denominator(self):
        return self._denominator
    
    @denominator.setter
    def denominator(self, denom):
        self._denominator = denom

    def __str__(self):
        return "{}/{}".format(self.numerator, self.denominator)

    def __repr__(self):
        return "{}/{}".format(self.numerator, self.denominator)

    def __eq__(self, other):
        return other.numerator == self.numerator and other.denominator == self.denominator


def reduce(num, denom):
    divisor = fractions.gcd(num, denom)
    if divisor > 1:
        toreturn = Fraction(num / divisor, denom / divisor)
    else:
        toreturn = Fraction(num, denom)
    return toreturn


def resilience(denom):
    fraction_set = [Fraction(num, denom) for num in range(1, denom)]
    reduced_fraction_set = map(reduce, [f.numerator for f in fraction_set], [f.denominator for f in fraction_set])
    fractions_cant_be_reduced = len([i for i, j in zip(fraction_set, reduced_fraction_set) if i == j])
    fraction = Fraction(fractions_cant_be_reduced, denom - 1)
    return reduce(fraction.numerator, fraction.denominator)


def denominators():
    denom = 94744
    cur_multiplicand = 1
    while True:
        yield denom * cur_multiplicand + 1
        cur_multiplicand += 1


for denom in denominators():
    resil = resilience(denom)
    if resil == Fraction(15499, 94744):
        print resil
        break
    else:
        print resili
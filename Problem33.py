import fractions
a = 10
b = 11
while b != 100:
    """print str(float(a)/float(b))
    print str(float(str(a)[:1])/float(str(b)[:1]))
    if fractions.Fraction(a, b) == fractions.Fraction(int(str(a)[:1]),int(str(b)[:1])):
        print str(a) + "/" + str(b) + " = " + str(a)[:1] + "/" + str(b)[:1]"""
    if str(a)[1:] != "0":
        if fractions.Fraction(a, b) == fractions.Fraction(int(str(a)[1:]),int(str(b)[:1])):
            print str(a) + "/" + str(b) + " = " + str(a)[1:] + "/" + str(b)[:1]
    if str(b)[1:] != "0":
        if fractions.Fraction(a, b) == fractions.Fraction(int(str(a)[:1]),int(str(b)[1:])):
            print str(a) + "/" + str(b) + " = " + str(a)[:1] + "/" + str(b)[1:]
    if a < (b - 1):
        a = a + 1
    else:
        a = 10
        b = b + 1
        

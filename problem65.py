class Fraction:
    def __init__(self, num, denom):
        self.num = num
        self.denom = denom

def wat(t):
    return str(t.num) + " / " + str(t.denom)

def sfat(thing):
    stuff = list(reversed(thing))
    #print map(wat, stuff)
    if len(stuff) <= 1:
        return Fraction(2 * stuff[0].denom + stuff[0].num, stuff[0].denom)
    newdenom = Fraction(stuff[1].denom * stuff[0].denom + stuff[0].num, stuff[0].denom)
    #print "* : " + wat(newdenom)
    new = Fraction(newdenom.denom * stuff[1].num, newdenom.num)
    #print "- : " + wat(new)
    if len(stuff) == 2:
        return Fraction(2 * new.denom + new.num, new.denom)
    else:
        del thing[-2]
        del thing[-1]
        thing.append(new)
        return sfat(thing[:])

fracts = []
for k in xrange(1,34):
    fracts.append(Fraction(1,1))
    print wat(sfat(fracts[:]))
    fracts.append(Fraction(1,k*2))
    print wat(sfat(fracts[:]))
    fracts.append(Fraction(1,1))
    print wat(sfat(fracts[:]))
    
print len(fracts)
thing = sfat(fracts[:])
print wat(thing)
print sum(map(int,list(str(thing.num))))

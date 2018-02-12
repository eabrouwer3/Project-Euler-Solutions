letters = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
triangles = [.5 * n * (n + 1) for n in xrange(1, 20)]

def wordScore(word):
    score = 0
    for letter in list(word):
        score += letters[letter]
    return score

a = []
f = open('words.txt', 'r')
words = sorted(f.read().lower().split('","'))
for word in words:
    if float(wordScore(word)) in triangles:
        a.append((word, wordScore(word)))

print a
print len(a)

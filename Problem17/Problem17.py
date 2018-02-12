from num2word import to_card
a = ""
for i in range(1, 1001):
    a = a + to_card(i)
a = a.translate(None, ' -')
print a
print len(a)

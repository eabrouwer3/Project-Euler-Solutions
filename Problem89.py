numerals = { 'I' : 1,
             'V' : 5,
             'X' : 10,
             'L' : 50,
             'C' : 100,
             'D' : 500,
             'M' : 1000 }

letters = [ 'M', 'D', 'C', 'L', 'X', 'V', 'I' ]
values = [1000, 500, 100, 50, 10, 5, 1]

def readNumeral(numeral):
    sets = []
    num = 0
    past = 1001
    for cur in numeral:
        if numerals[cur] > past:
            num = (num - past) + (numerals[cur] - past)
            past = numerals[cur]
        elif numerals[cur] <= past:
            num = num + numerals[cur]
            past = numerals[cur]
    return num

def simplifyNumeral(num):
    numeral = ''
    for val, letter in zip(values, letters):
        if num / val >= 1:
            numeral = numeral + (letter * (num / val))
            num = num - val * (num / val)
        if num >= 900 and num < 1000:
            numeral = numeral + letters[2] + letters[0]
            num = num - 900
        if num >= 400 and num < 500:
            numeral = numeral + letters[2] + letters[1]
            num = num - 400
        if num >= 90 and num < 100:
            numeral = numeral + letters[4] + letters[2]
            num = num - 90
        if num >= 40 and num < 50:
            numeral = numeral + letters[4] + letters[3]
            num = num - 40
        if num >= 9 and num < 10:
            numeral = numeral + letters[6] + letters[4]
            num = num - 9
        if num >= 4 and num < 5:
            numeral = numeral + letters[6] + letters[5]
            num = num - 4
    return numeral

f = file('roman.txt')
nums = [n for n in f.read().split('\n')]
newNums = []
old = len(str(nums))
print old
for n in nums:
    num = readNumeral(n)
    numeral = simplifyNumeral(num)
    newNums.append(numeral)
new = len(str(newNums))
print new
print old - new
print newNums[:20]
print nums[:20]

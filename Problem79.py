f = open('keylog.txt', 'r')
nums = sorted(list(set(f.read().split('\n'))))
print nums

for num in nums:
    print num

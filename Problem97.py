exponent = 7830457
mod = 10000000000
multiplier = 28433

a = 1

while exponent > 0:
    if exponent < 50:
        a = a * (2**exponent % mod)
        exponent = 0
    else:
        exponent = exponent - 50
        a = a * (2**50 % mod)

print str((multiplier * (a % mod) + 1) % mod)

def is_prime(num):
    for i in xrange(2, num):
        if (num % i == 0):
            return 0
    return 1

import random
rand = random.randrange(10)
print rand
if is_prime(rand) == 1:
    print rand
 

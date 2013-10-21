__author__ = 'Administrator'


"""some comments
"""
def sqrt(x):
    squre = 0

    if x > 0:
        while (squre * squre < x):
            squre += 1
        if squre * squre != x:
            print x, 'is not prefect squre'
        else:
            print squre
    else:
        print x, "is not good"

print sqrt(36)

counter = 10
for i in range(1,counter):
    if counter %i == 0:
        print 'div', i

xx= 100
divisors = ()
for i in range(1,xx):
    if xx%i == 0:
        divisors = divisors + (i,)
print divisors

sumDigits = 0
for c in str(1952):
    sumDigits += int(c)
print sumDigits
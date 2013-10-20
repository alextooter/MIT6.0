__author__ = 'Administrator'

x = 15

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
__author__ = 'Administrator'

# this is for class two.
x = 15
if (x / 2) * 2 == x:
    print 'Even'
else:
    print 'Odd'

a = 14
b = 11
c = 8

if a > b:
    if b > c:
        print 'c is smallest'
    else:
        print 'b is smallest'
else:
    if a > c:
        print 'c is smallest'
    else:
        print 'a is smallest'


if a<b and a < c:print 'a is least'
elif b<c: print 'b is least'
else: print 'c is least'


y = 0
x = 3

intersLeft = x
while(intersLeft > 0):
    y += x
    intersLeft -= 1
print y
__author__ = 'alex'

shoplist=['apple','mango','carrot','banana']

print 'i have', len(shoplist), 'items to purchase'

shoplist.append('rice')

shoplist.sort()

del shoplist[0]
for i in shoplist:
    print i

zoo=('wolf','elephant','penguin')

print 'number of animals in the zoo is ', len(zoo)

new_zoo =('monkey','dolphin', zoo)

print new_zoo[2]

ab={'alex':'alextooter@gmail.com',
    'tooter':'tooter@163.com'}

print ab['alex']

del ab['tooter']

print ab

for name, addr in ab.items():
    print name,addr


shoplist1=['apple','mango','carot','banana']

print 'item 0 is', shoplist1[0]
print 'item 1 is', shoplist1[1]
print 'item 2 is', shoplist1[2]
print 'item 3 is', shoplist1[3]
print 'item -1 is', shoplist1[-1]
print 'item -2 is', shoplist1[-2]

print 'item 1 to 3 is ', shoplist1[1:3]
print 'item 2 to end is ', shoplist1[2:]
print 'item 1 to -1 is ', shoplist1[1:-1]

"""20 heads, 56 legs
pig+checken = 20
4*pig+2*checken = 56"""


def PigAndChecken (head, leg):
    for pig in range(0,head):
        for checken in range(0, head):
            if pig + checken == head and pig*4 + checken*2 == leg:
                return (pig, checken)
    else:
        return (None, None)

print PigAndChecken(20,56)

	

def isRec (string):
    if len(string) <= 1: return True
    else:
        return string[0] == string[-1] and isRec(string[1:-1])

print isRec('abcba')

def fib(x):
    if x == 0 or x == 1: return 1
    else:
        return fib(x-1) + fib (x-2)

print fib(35)

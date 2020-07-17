from cmath import *
a = float(input('a? ')); b = float(input('b?')); c= float(input('c?'))

def solve1(a,b,c):
    del1 = -b+sqrt(b**2-4*a*c)
    del2 = 2*a
    res = del1/del2
    return res
def solve2(a,b,c):
    del1 = -b-sqrt(b**2-4*a*c)
    del2 = 2*a
    res = del1/del2
    return res
print('losninger: {} , {}'.format(solve1(a,b,c),solve2(a,b,c)))

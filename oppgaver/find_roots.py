from cmath import *

a = float(input("ax^2: "))
b = float(input("bx: "))
c = float(input("c: "))
try:
    s1 = ((-1*b)+sqrt((b**2)-(4*a*c))/(2*a))
    s2 = ((-1*b)-sqrt((b**2)-(4*a*c))/(2*a))
    print("first root: {}, second root {}".format(s1,s2))
except:
  print("no rasinoal factors")

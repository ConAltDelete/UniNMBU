from math import *

def rectify(x):
    if sin(x)>0:
        return sin(x)
    elif sin(x)<=0:
        return 0
    else:
        pass

def test_rectify():
    x = (1,10,100,46,9)
    expected = (sin(1),0,0,sin(46),sin(9))
    computed = [rectify(i) for i in x]
    tol = 1e-14
    for z in zip(expected,computed):
        test = abs(z[0] - z[1]) < tol
        assert test
test_rectify()
'''
python half_wave.py
'''

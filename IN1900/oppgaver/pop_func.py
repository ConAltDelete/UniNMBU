from math import *

def N(t,k,B,C):
    del1 = B
    del2 = (1+C*exp(-k*t))
    funk = del1/del2
    return funk

def test_N():
    t=0;C=9;k=0.2;B=50000
    expected = 5000
    computed = N(t,k,B,C)
    tol = 1e-14
    test = abs(expected - computed) < tol
    assert test
test_N()
'''
$ python pop_func.py
'''

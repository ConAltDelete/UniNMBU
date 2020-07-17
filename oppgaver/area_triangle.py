# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 19:37:13 2018

@author: matsh
"""

def triangle_area(cor): #definerer funksjon
    vertices = cor #oppdaget variabel bytte
    aria = 0.5*(vertices[1][0]*vertices[2][1]-vertices[2][0]*vertices[1][1] \
        -vertices[0][0]*vertices[2][1]+vertices[2][0]*vertices[0][1]+ \
        vertices[0][0]*vertices[1][1]-vertices[1][0]*vertices[0][1])#Arial formel med hjelp av 2 liter sterk te
    return aria #jeg vet at arial ikke staves aria, men 'aria' er søtere

def test_triangle_area():
    """
    Verify the area of a triangle with vertex coordinates
    (0,0), (1,0), and (0,2).
    """
    v1 = (0,0); v2 = (1,0); v3 = (0,2)
    vertices = [v1, v2, v3]
    expected = 1
    computed = triangle_area(vertices)
    tol = 1E-14
    success = abs(expected - computed) < tol #måtte fjerne diff() for å få dette til å fungere
    msg = "computed area=%g != %g (expected)"% \
        (computed, expected)
    assert success, msg
print(test_triangle_area()) #starter formel

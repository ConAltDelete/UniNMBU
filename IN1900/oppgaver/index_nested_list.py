# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 13:39:54 2018

@author: matsh
"""

q = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h']]

#a,[d,e,f],h

print(q[0][0])
print(q[1])
print(q[-1][-1])
print("")
for i in q:
    for j in range(len(i)):
        print (i[j])
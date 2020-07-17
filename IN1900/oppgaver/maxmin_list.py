# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 15:47:25 2018

@author: matsh
"""

def Max(a):

        l = a[0]
        for x in a:
            if x > l:
                l = x
            elif x <= l:
                pass
            else:
                l = "uforventet tall"
                break
        return l


def Min(a):

        m = a[0]
        for x in a:
            if x < m:
                m = x
            elif x >= m:
                pass
            else:
                m = "uforventet tall"
                break
        return m


q = [1,2,3,4,5,3]

print (Max(q))
print (Min(q))
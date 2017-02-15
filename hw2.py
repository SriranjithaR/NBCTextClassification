# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 17:55:03 2017

@author: Sriranjitha
"""
import numpy as np

a = [[20,1,1],[15,0,1],[5,0,0]];

print np.sum(a,axis=0)

b = np.add(a,1)


print b
print b.transpose()
print b
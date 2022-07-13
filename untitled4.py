# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 15:25:14 2022

@author: USER
"""
def radian(p1,p2,p3):
    l1 = p2-p1
    l2 = p3-p2
    return math.acos(Inner2D(l1,l2))

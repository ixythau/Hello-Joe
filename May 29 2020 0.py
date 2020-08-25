#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 26 11:26:21 2020

@author: test
"""
#grange = 0
#grange = []
#print(type(grange))
##print(type(grange))
#for x in range(21):
#    if x != 17:
#        grange = x
# So do I need a driver here to fill values into list - grange?
#       # print(grange)
#print( grange)
#
#while grange < 28:
#    print(grange)
#    grange += 1
    
#---------------------------------------------------------------
# I found this i looking for how t0 set values to a list!
#n = [ 0 for n in range(30)]
#print(n)
#for r in range(30):
#    n = r
##    print(n)
#print(n)
#---------------------------------------------------------------
# source http://zetcode.com/lang/python/lists/
# Python lists

#n1 = [0 for i in range(15)]
#n2 = [0] * 15
#
#print(n1)
#print(n2)
#
#n1[0:11] = [10] * 10
#
#print(n1)
#======================================================

num = 5 #once again, ifs dont loop so output is 5,4
if num > 2:
    print(num)
    num -= 1
print(num)
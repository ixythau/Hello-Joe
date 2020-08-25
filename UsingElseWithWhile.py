#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 16:21:26 2020

@author: test

Issues using a else with a While?
"""

#Else clause on python while statement?
#https://stackoverflow.com/questions/3295938/else-clause-on-python-while-statement

#n = 5
#while n != 0:
#    print (n)
#    n -= 1
#else:
#    print (n,"what the...")


for k in [2, 3, 5, 7, 11, 13, 17, 25]:
    for m in range(2, 10):
        if k == m:
            continue #smaller, faster gear turning a larger one? Is this how
           # searching a string works? """
        print ('trying %s %% %s' % (k, m) )
        if k % m == 0:
            print ('found a divisor: %d %% %d; breaking out of loop' % (k, m))
            break
    else:
        continue
    print ('breaking another level of loop')
    break
else:
    print ('no divisor could be found!')
#    
#    
#for value in range(18):
#    if value == 5:
#        print ("Found it!")
#        break
#    else:
#        print (value,"Nowhere to be found. :-(")
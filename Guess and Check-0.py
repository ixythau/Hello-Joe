#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 13:10:05 2020

@author: test
"""

#x = int(input("Enter a number and I'll see if it's a perfect cube  :"))
#ans = 1
#while ans**3 < x:
#    ans += 1# 
#if ans**3 >x:
#    print('bad guess space cadet!!', ans)
#else:
#    print( 'yup, the cube root of' , x , ' is ')
    
    
    # floating point investigation of similar thing!
    
x = int(input("Enter a number and I'll see if it's near perfect cube  :"))
ans = 0
while ans**3 < x:
    ans += .000011 # the more zeros added the longer it takes to calculate!
if (ans**3 - x) < .0002: # Seems I have to specific the limits of aaccuracy !
   # print('bad guess space cadet!!', ans)

    print( 'yup, the cube root of' , x , ' is ', ans)
    
""" Note, much like the phone book example in the Harvard intro to computers course,
the greater granularity to variable answer, less chance I miss with .0002 re-
solution. But how to configure both?  There must be some ration. 

Take a look at accuracy and precision
"""
    
#x = (int(input(' Giimme a number bigger than 5  ')))
#while(x >= 4):
#    x = x-1
#    print(x)
#print('shucks!!!', x)


        

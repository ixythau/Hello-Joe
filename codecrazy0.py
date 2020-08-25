#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  7 14:10:02 2020

@author: test
"""
""" So to get the loop occuring, I broke the problem into right answer and wrong.
the wrong answer is where the loop exists.

Still, there is a problem with this programs execution """
# 
#value = int(input('Enter a value <= 5  '))
#if value <= 5:
#        print(value, '\n\n\t Nice Job!')
##else:
#oops = value
##    print('\tshit head!!  I said < 5. \n\n\t\t TRY AGAIN!!!!!!' )
#while value > 5:
#
#    value = int(input('Enter a value <= 5  '))
#    if value <= 5:
#            print(value, '\n\n\t Nice Job!')
#    else:
#            print('\tshit head!!  I said < 5. \n\n\t\t TRY AGAIN!!!!!!' )
#              
#    """ The above program acts in sto stages but I want it to happen as one. """

#        Program II below.

value = int(input('Enter a value Less than or equal to 5  '))
if value <= 5:
        print(value, '\n\n\t Nice Job!')
else:
    oops = value
    print('\t NO!!!! shit head!!  I said less than 5. \n\n\t\t TRY AGAIN!!!!!!' )
while value > 5:

    value = int(input('Enter a value <= 5  '))
    if value <= 5:
            print(value, '\n\n\t Nice Job!')
    else:
            print('\tshit head!!  I said < 5. \n\n\t\t TRY AGAIN!!!!!!' )
                  
        
""" Not bad. but how about some further refinement. Reading input & determining
if it's incorrect

Note that we've not been taught while statements yet.  so how would you do this
 with if...else?"""
 
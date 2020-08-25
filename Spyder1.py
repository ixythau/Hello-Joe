# -*- coding: utf-8 -*-
"""
Spyder Editor
How to compile and run on spyder:
    https://www.google.com/search?q=how+to+compile+and+run+on+spyder&oq=how+to+compile+and+run+on+spyder&aqs=chrome..69i57j69i64.9655j0j7&sourceid=chrome&ie=UTF-8
        https://www.southampton.ac.uk/~fangohr/blog/spyder-the-python-ide.html 
This is a temporary script file.
"""

x = float(input("Enter a number for x:"   ))
y = float(input("Enter a number for y:"  ))

if x == y:
    print("x and y are equal!")
    if y!=0:
        print("therefor x/y is,   ", x/y)
        
elif x < y:
    print("x is smaller")
    
else:
    print("y is smaller!")
    
print("bye")




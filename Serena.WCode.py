# -*- coding: utf-8 -*-
""" 
Created on Mon Jun 10 16:08:25 2019

@author: admin
"""
#Documentation 
#need perentaces when using words and quotes
#number does not need quotes 
#exponent=**

# steps for function
# 1)define by giving a name and perameters
# 2)action
# 3)test your function 

# pi = 3.14 or 22/7
# e = 2.7
# power funtion, squareroot, factorial are not scaler 
# scaler are numbers that stay the same 
# factorial = 5!=5*4*3*2*1

# wrinting code to sum any two number 

def sum(a,b): 
    sum = a + b
    
    print("the sum of",a,"and",b,"is",sum)
    
sum(4,5)
sum(3.6,4.9)

# wrinting code to sum any three number 

def sum(a,b,c):
    sum = a + b + c
    
    print("the sum of",a,"and",b,"and",c,"is",sum)
    
sum(4,5,6)
sum(6.2,7.6,8.6)

# area of triangle

def multiplication(b,h):
    multiplication = 0.5*b*h

    print("the multiplication of",b,"and",h,"is",multiplication)
    
multiplication(4,5)
multiplication(41,9)

# how to greet

def greet(a):
    greet = a 
    
    print("Hello",greet)
    
greet("serena")

def greeting(b):
    greeting = b
    
    print(greeting)
    
greeting("how are you doing?")
    
# use "import math" to import file

import math
dir(math)

math.pi
# e = the sign e 
math.e
# when doing non scaler you will need to put in perentaces
math.sqrt(4)
# math factorial is the multiplecation of the number
math.factorial(100)
math.pow(3,10)
math.remainder(4,6)
math.remainder(10,6)

def cubicroot(c):
    cubicroot = c
    
    print(math.pow(c,(1/3)))
    
cubicroot(8)

def cuberoot(d):
    cuberoot = d**(1/3)
    
    print(cuberoot)
    
cuberoot(8)

5/8 #Division
print("Hello",5,"World")
print("I love Python")
print("I learned to code python today")
print(5)
5*2 # 5 multiplied by 2
5/2 # 5 divide by 2
5-2 # 5 subtracted by 2
5**2 # 5 raised to the power of 2
(8/9)*3 # 8 divide by 9 multiplied by 3 



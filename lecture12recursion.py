#sumation of 1 to n by using recursion
"""num=int(input("enter number"))
def summation(n):
    if n==1:
        return 1
    sum=n+summation(n-1)
    
    return sum
r=summation(num)
print(r)

#factorial of 1 to n using recursion

number=int(input("enter number:"))
def multiplication(n1):
    if n1==1:
        return 1
    mult=n1*multiplication(n1-1)
    return mult
g=multiplication(number)
print(g)
"""
#global scope

x=10
def globalscope():
    print("value of x inside function:",x)
globalscope()
print("value of x outside function:",x)


#local scope

def localscope():
    y=10
    print("value of y inside fuction :",y)
localscope()

#modules
"""
import math
n=int(input("enter n:"))
print("factorial of n is",math.factorial(n))

import math as m
num=float(input("enter number:"))
print("ceil of number is:",m.ceil(num))

from math import factorial,sqrt
number=int(input("enter number"))
um1=int(input("enter value"))
print("facctorial of number is:",math.factorial(number))
print("square root of number is:",math.sqrt(um1))"""

import string
print("letters",string.ascii_letters)
print("all letters",string.ascii_lowercase)
print("letters",string.ascii_uppercase)
print("digits:",string.digits)
numb=int(input("enter number"))
print("digits to show are:",string.digits(numb))

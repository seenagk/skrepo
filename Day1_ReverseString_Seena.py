# Day 1: Problem 1 : Reverse a string :BY: Seena K

# This is a program to reverse strings in Python.
#---------------------------------------------------------------------------
x=str(input("Please Enter a String: "))
y = len(x)

# While Loop

i=1
j=0

z= x[-i:]

while i <=y:
    i=i+1
    j=j+1
    z1=(x[-i:-j])
    z=(z+z1)

print(z)

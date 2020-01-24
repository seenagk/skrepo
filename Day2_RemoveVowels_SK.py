#-------------------------------------------------------------------------------
# Day 2: Remove Vowels from a String
#-------------------------------------------------------------------------------

print("This program will remove the vowels from a string")
print("Please Enter a String")

x = str(input())
print(x)

print("The string without the vowels are: ")

y1= x.replace("a", "")
y2 = y1.replace("e","")
y3 = y2.replace("i","")
y4 = y3.replace("o","")
y5=  y4.replace("u","")

print(y5)
#-------------------------------------------------------------------------------


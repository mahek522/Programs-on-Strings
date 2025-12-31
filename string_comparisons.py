#Implementing different string comparisons in python

#Comparison based on values
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
if str1 == str2:
    print("String values are equal")
else:
    print("String values are unequal")
    
    
    
#Comparison based on references
if id(str1) == id(str2):
    print("Both strings reference the same object in memory")
else:
    print("String references are different")
    
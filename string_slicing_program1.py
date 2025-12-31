#Program to print all the characters of a string except the first and last character.
string = input("Enter a String: \n")
print("String after removing first and last character is:")
print(string[1:len(string)-1])
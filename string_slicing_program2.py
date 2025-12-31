#Program to print all the characters of a string except the first and last character. in reverse order.
string = input("Enter a String:\n")
print("String after removing first and last character in reverse order is:")
print(string[len(string)-2:0:-1])

#Program to check whether a given string is a palindrome or not.
string = input("Enter a String: \n")
if string == string[::-1]:
    print(string,"string is a Palindrome")
else:
    print(string,"string is not a Palindrome")
#Program to swap cases of all characters in a given string.
string = input("Enter a String: \n")
swapped_string = ""
for char in string:
    if ord(char) >=97 and ord(char) <=122: #Check for lowercase letters
        swapped_string += chr(ord(char)-32)
    elif ord(char) >=65 and ord(char) <=90: #Check for uppercase letters
        swapped_string +=chr(ord(char)+32)
    else:
        swapped_string += char
print("String after swapping cases : ", swapped_string)
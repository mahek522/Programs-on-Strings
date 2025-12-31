#Program to print all the substrings of a given string whose length is 3
string = input("Enter a String: \n")
print("Substrings of length 3 are:")
for i in range(0,len(string)-2):
    print(string[i:i+3])
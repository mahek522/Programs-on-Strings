#reverse_second_half_of_string.py
#Program to reverse the second half of a given string.
string = input("Enter a String: \n")
mid = len(string)//2
print("String after reversing the second half is:", string[:mid:] + string[len(string)-1 :mid-1:-1])
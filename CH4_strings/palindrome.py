# Check if string is a palindrome
# The input is checked for errors and punctuation is removed first

string = ""
string = input("Insert a palindrome string here: ")

palindrome = True
check_len = len(string)//2
i = 0

while i in range(check_len) and palindrome:
    if string[i] != string[-(i+1)]:
        palindrome = False
    i += 1

if palindrome:
    print(string, "is a palindrome")
else:
    print(string, "is not a palindrome")
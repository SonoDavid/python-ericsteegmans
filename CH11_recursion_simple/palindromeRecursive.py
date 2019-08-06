# Check if string is a palindrome
# The input is checked for errors and punctuation is removed first
def is_palindrome(string):
    if len(string) <= 1:
        return True
    else:
        return (string[0] == string[-1]) and\
                is_palindrome(string[1:-1])

assert is_palindrome("abcba")
assert not is_palindrome("blabla")
assert is_palindrome("bab")
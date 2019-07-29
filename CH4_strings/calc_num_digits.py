# Calculate the sum of the digits in an integer number
# in decimal format
#   - The program keeps on prompting for a non-negative
#     integer number until it finally gets one

number = ""
while not str.isdigit(number):
    number = input\
        ("Enter a non-negative number: ")

digit_sum = 0
current_pos = 0

while current_pos < len(number):
    digit_sum += ord(number[current_pos]) - ord("0")
    current_pos += 1

print("The sum of the digits of the number",\
    number,"amounts to",digit_sum)
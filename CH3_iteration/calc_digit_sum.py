#Calculate the sum of the digits in an integer number
# in decimal format
#    The program keeps on prompting for a non-negative
#    integer nuber until it finally gets one

number = ""
while not str.isdigit(number):
    number = input\
        ("Enter a non-negative integer number: ")
number = int(number)

print("The sum of the digits of the number",\
    number, end=" ")

digit_sum = 0

while number > 0:
    digit_sum += (number % 10)
    number = number // 10

print("amounts to:", digit_sum)
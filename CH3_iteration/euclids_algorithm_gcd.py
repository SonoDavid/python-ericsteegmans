# Apply Euclids algorithm for the 
# Greatest Common Divisor
#    From two numbers, derive a new pair that
#    consists of the smaller number and the difference
#    between the two numbers. Repeat until both numbers are equal.
#    That is the greatest common divisor
#    of the original pair of integer numbers

def get_number():
    number = ""
    while not str.isdigit(number):
        number = input\
            ("Enter a non-negative integer number: ")
    number = int(number)
    return number

number1 = get_number()
number2 = get_number()

print(number1, "and",
      number2, end=" ")

while number1 != number2:
    smallest = min(number1, number2)
    diff = abs(number1-number2)
    number1 = smallest
    number2 = diff

print("has Greatest Common Divisor (GCD):", number1)
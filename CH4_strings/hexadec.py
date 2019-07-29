# Write the hexadecimal representation in Python
# form the hex representation from a digit

number = ""
stop = False
while not number.isdigit():
    number = input("Insert an integer number: ")
    old_number = number
    if number.startswith("-"):
        add_minus = True
        number = number[1:]
    else:
        add_minus = False

number = int(number)

i = 16
hexa = ""

while number > 0:
    if number % i != 0:
        rest = number % i
        if rest >= 10:
            char = chr(ord("a") + (rest-10))
        else:
            char = str(rest)
        print(char)
        hexa = char + hexa
        number = number - rest
        number = number // 16
if hexa == "":
    hexa = "0"
hexa = "0x" + hexa
if add_minus:
    hexa = "-" + hexa


print('The hex representation of', old_number, 'is', hexa)
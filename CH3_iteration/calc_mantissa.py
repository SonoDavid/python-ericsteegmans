# Joachim David - July 2019
# Calculate binary representation of the mantissa of
# a floating point number.
# First made in pseudo-code on paper

fp_number = ""
mantissa_bits = ""

while not str.isdigit(mantissa_bits) or not fp_number.startswith("0.")\
      or not str.isdigit(fp_number[2:]):
      fp_number = input("Enter a floating point number to calculate mantissa: ")
      mantissa_bits = input("Enter the number of bits for mantissa: ")

fp_number = float(fp_number)
mantissa_bits = int(mantissa_bits)

outp = "0."
it = 1
rem = fp_number

while mantissa_bits > 0:
    if rem >= 2**-it:
        outp += "1"
        rem -= 2**-it
    else:
        outp += "0"
    it += 1
    mantissa_bits -= 1

if rem > 2**-it:
    outp = outp[:-1] + "1"

print(f"The mantissa of the number {fp_number} is {outp}")
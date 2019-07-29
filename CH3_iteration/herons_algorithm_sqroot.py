# Calculate the square root of a given number
#    - The programm assumes it can read a non-negative
#      number that is not infinite
#    - The program prints an approximation of the square
#      root of that number. The difference in absolute
#      value beteen the squared approximation and the
#      given number does not exceed 1.0E-200, unless the
#      program signals otherwise.

number = float(input("Enter a non-negative number: "))

PRECISION = 0.1E-200

prev_approx  = 1.0
approx_root = (1.0 + number) / 2.0

while(abs(approx_root*approx_root - number) >\
       PRECISION) and (prev_approx!=approx_root):
    prev_approx = approx_root
    approx_root =\
        (prev_approx + number/prev_approx)/2

print("sqrt(", number, ") =", approx_root)
if abs(approx_root*approx_root - number) > PRECISION:
    print(" Precision probably not reached!")

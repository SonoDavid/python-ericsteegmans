# Calculate the body mass index of some person.
#   - The body mass index is obtained from the formula
#     (weight/height**2).
#   - The weight must be expressed in kilograms;
#     the height in meters.

weight = float(input('Enter the weight: '))
height = float(input("Enter the height: "))

bmi = weight / height**2

if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi < 25.0:
    category = "Normal"
elif 25.0 <= bmi <= 30.0:
    category = "Overweight"
else:
    category = "Obese"

print("BMI", bmi, "[", category, "]")